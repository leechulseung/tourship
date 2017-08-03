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

@user_passes_test(lambda user : not user.is_authenticated, login_url='index')
def joinus(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/joinus.html' ,{
        'form':form
        })
flag= True
@login_required
def set_up(request):
    global flag
    if request.method == "POST":
        if flag:
            form = CheckForm(request.user,request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                seo_specialist =  authenticate(username=username, password=password)
                if seo_specialist is not None:
                    flag =False
                else:
                    flag=True
        else:
            form = SetupForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                flag=False
    elif request.method == "GET":
        form = CheckForm(request.user,request.POST)
    return render(request, 'accounts/set_up.html',{
        'form':form,
        })

@login_required
def sign_out(request):
    return render(request, 'accounts/sign_out.html')


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

def friend_accept(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.accept()
    return redirect('friend_list')

def friend_reject(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.reject()
    return redirect('friend_list')

def friend_cancel(request,pk):
    f_request = get_object_or_404(FriendshipRequest, id=pk)
    f_request.cancel()
    return redirect('friend_list')

