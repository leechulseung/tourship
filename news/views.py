import json
from django.shortcuts import render, HttpResponse , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, CommentForm

@login_required
def news_list(request):
    post_list = Post.objects.all().order_by('-id')
    form = CommentForm(request.POST or None)

    search = request.GET.get('search', None)
    real_time = request.GET.get('real', None)
    if search:
        post_list = post_list.filter(title__icontains=search)

    if request.is_ajax():
        pk = request.POST.get('pk', None)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            com= form.save(commit=False)
            com.author = request.user
            com.post = post
            com.save()
            return render(request,'news/news_list_ajax.html',{
                'comment':com
                })
    return render(request, 'news/news_list.html',{
        'post_list':post_list,
        'form':form,
        })

@login_required
def news_update(request):
    pass

@login_required
def news_destroy(request):
    pk = request.POST.get('pk', None)
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponse('clear')

def news_like(request):
    pk = request.POST.get('pk', None)
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)
 
    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message,
               'nickname': request.user.first_name }
    return HttpResponse(json.dumps(context))
