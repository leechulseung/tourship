from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def news_list(reqeust):
    return render(reqeust, 'news/news_list.html')
