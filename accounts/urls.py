from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^joinus/$', views.joinus, name="joinus"),
    url(r'^index/$', views.index ,name="index"),
    url(r'^set_up/$', views.set_up, name="set_up"),
    url(r'^sign_out/$', views.sign_out, name="sign_out"),
    url(r'^friend/(?P<pk>\d+)?$', views.friend_list, name="friend_list"),
    url(r'^friend_add/(?P<pk>\d+)$', views.friend_accept, name="friend_add"),
    url(r'^friend_reject/(?P<pk>\d+)$', views.friend_reject, name="friend_reject"),
    url(r'^friend_cancel/(?P<pk>\d+)$', views.friend_cancel, name="friend_cancel"),
]