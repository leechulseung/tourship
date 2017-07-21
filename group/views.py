from django.shortcuts import render

#그룹 메인화면 
def group_index(request):
    return render(request, 'group/group_index.html')

#그룹 생성하기 
def group_make(request):
    return render(request, 'group/group_make.html')

#그룹별 게시판
def group_book(request):
    return render(request, 'group/group_tourbook.html')

