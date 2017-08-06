from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

#allauth
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

#Form
from .forms import LoginForm, SignUpForm, PostForm, CheckForm, SetupForm

#Post
from news.models import Post

#friend
from friendship.models import Friend, FriendshipRequest

from .signals import certified_update

@user_passes_test(lambda user : not user.is_authenticated, login_url='index')
def login(request):
    providers =[]
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app= None
        providers.append(provider)
        
    return auth_login(request,
        authentication_form= LoginForm,
        template_name='accounts/login.html',
        extra_context = {'providers': providers}
        )

@login_required
def index(request):
    post_list = Post.objects.all().filter(author=request.user)
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if request.FILES:
            fiels= request.FILES.getlist('photo', None)
        post =form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('news:news_list')

    return render(request, 'accounts/index.html',{
        'form':form,
        'post_list':post_list,
        })

@user_passes_test(lambda user : not user.profile.is_authenticated, login_url='index')
def joinus(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/joinus.html' ,{
        'form':form
        })

@login_required
def setup_auth(request):
    if request.method == "POST":
        form = CheckForm(request.user, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_info =  authenticate(username=username, password=password)
            if user_info is not None:
                user=request.user
                request.user.profile.is_certified = True
                request.user.profile.save()
                return redirect('setup')
    elif request.method == "GET":
        form = CheckForm(request.user)
    return render(request, 'accounts/set_up.html',{
        'form':form,
        })

certified = lambda user : user.profile.is_certified

@login_required
@user_passes_test(certified, login_url='setup_auth')
def setup(request):
    request.user.profile.is_certified=False
    request.user.profile.save()
    if request.method == "POST":
        form = SetupForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    elif request.method == "GET":
        form = SetupForm(user=request.user, data=request.POST)
    return render(request, 'accounts/set_up.html',{
        'form':form,
        })

@user_passes_test(certified, login_url='setup_auth')
@login_required
def sign_out(request, pk):
    if pk:
        user = request.user
        user.delete()
    return render(request, 'accounts/sign_out.html')

@login_required
def friend_list(request, pk):
    request_s = Friend.objects.requests(request.user)
    sent_requests = Friend.objects.sent_requests(request.user)
    friendlist= Friend.objects.friends(request.user)
    
    sent_requests_list=[u.to_user for u in sent_requests]

    user= get_user_model()
    user = user.objects.all()
    
    if pk:
        to_user = user.get(pk=pk)
        from_user = request.user
        Friend.objects.add_friend(from_user,to_user)
        return redirect('friend_list')
    return render(request, 'accounts/friend.html',{
        'user_list':user,
        'requests':request_s,
        'sent_requests':sent_requests,
        'friend_list':friendlist,
        'sent_requests_list':sent_requests_list,
        })

@login_required
def friend_accept(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.accept()
    return redirect('friend_list')

@login_required
def friend_reject(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.reject()
    return redirect('friend_list')

@login_required
def friend_cancel(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.cancel()
    return redirect('friend_list')

