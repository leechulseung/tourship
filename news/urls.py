from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list , name="news_list"),
    url(r'^destroy/$', views.news_destroy, name="destroy"),
    url(r'^update/$', views.news_update, name="update"),
    url(r'^like/$', views.news_like, name='post_like'),
    url(r'^modal/$', views.news_modal, name='modal'),
    url(r'^comment_more/$', views.news_comment_more, name="comment_more"),
]