from django.shortcuts import render

#index_all 모든 유저가 보는 메인 페이지
#회원이 보는 메인 페이지

def login(request):
    return render(request, 'accounts/login.html')

def index(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'accounts/index.html')

def joinus(request):
    return render(request, 'accounts/joinus.html')


def set_up(request):
    return render(request, 'accounts/set_up.html')

def sign_out(request):
    return render(request, 'accounts/sign_out.html')