from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
#allauth 
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
#Form
from .forms import LoginForm, SignUpForm, PostForm
#Post
from news.models import Post


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
    form = PostForm(request.POST or None)
    if form.is_valid():
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

@login_required
def set_up(request):
    return render(request, 'accounts/set_up.html')

@login_required
def sign_out(request):
    return render(request, 'accounts/sign_out.html')