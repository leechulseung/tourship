from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
#index_all 모든 유저가 보는 메인 페이지
#회원이 보는 메인 페이지

@user_passes_test(lambda user : not user.is_authenticated, login_url='index')
def login(request):
    return render(request, 'accounts/login.html')

@login_required
def index(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'accounts/index.html')
    
@user_passes_test(lambda user : not user.is_authenticated, login_url='index')
def joinus(request):
    return render(request, 'accounts/joinus.html')

@login_required
def set_up(request):
    return render(request, 'accounts/set_up.html')

@login_required
def sign_out(request):
    return render(request, 'accounts/sign_out.html')