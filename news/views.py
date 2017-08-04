import json
from django.db.models import F,Q
from django.shortcuts import render, HttpResponse , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, CommentForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required
def news_list(request, template='news/news_list.html',
    page_template='news/page_list.html',
    message_template='news/news_list_ajax.html'):

    #17.07.31 중복제거를 위해 distinct()추가
    post_list = Post.objects.order_by('-created_at').filter(Q(author=request.user) | Q(privacy__policy='전체공개') | Q(author__friends__from_user=request.user) | Q(author__friends__to_user=request.user)).distinct()
    form = CommentForm(request.POST or None)

    search = request.GET.get('search', None)
    real_time = request.GET.get('real', None)
        
    if search:
        post_list = post_list.filter(title__icontains=search)

    post_list=post_list.select_related('author').prefetch_related('news_comments__author','like_set','author__friends')
    paginator = Paginator(post_list, 3)
    page_num = request.POST.get('page')

    try:
        posts= paginator.page(page_num)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_page)
    
    context = {
        'posts':posts,
        'form':form,
    }
    if request.is_ajax():
        if request.POST.get('message',None):
            pk = request.POST.get('pk', None)
            print(pk)
            post = get_object_or_404(Post, pk=pk)
            if form.is_valid():
                com= form.save(commit=False)
                com.author = request.user
                com.post = post
                com.save()
                template = message_template
                context={'comment':com}
        else:
            template=page_template
            context={
            'posts':posts,
            'form':form,
            }
    return render(request, template ,context)

def news_modal(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post=post)
    form=CommentForm()
    return render(request, 'news/news_modal.html',{
        'post':post,
        'comments':comment,
        'form':form,
        })

def news_comment_more(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    if request.is_ajax():
        comments = Comment.objects.filter(post=post)[4:]
        return render(request,'news/comment_more_ajax.html',{
            'comments':comments,
            })
    return redirect("news:news_list")   

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
