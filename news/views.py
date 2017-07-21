from django.shortcuts import render

def news_list(reqeust):
    return render(reqeust, 'news/news_list.html')
