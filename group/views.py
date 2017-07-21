from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#그룹 메인화면 
@login_required
def group_index(request):
    return render(request, 'group/group_index.html')

#그룹 생성하기
@login_required
def group_make(request):
    return render(request, 'group/group_make.html')

#그룹별 게시판
@login_required
def group_book(request):
    return render(request, 'group/group_tourbook.html')

