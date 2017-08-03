from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^joinus/$', views.joinus, name="joinus"),
    url(r'^index/$', views.index ,name="index"),
    url(r'^setup_auth/$', views.setup_auth, name="setup_auth"),
    url(r'^setup/$', views.setup, name="setup"),
    url(r'^sign_out/(?P<pk>\d+)?$', views.sign_out, name="sign_out"),
    url(r'^friend/(?P<pk>\d+)?$', views.friend_list, name="friend_list"),
    url(r'^friend_add/(?P<pk>\d+)$', views.friend_accept, name="friend_add"),
    url(r'^friend_reject/(?P<pk>\d+)$', views.friend_reject, name="friend_reject"),
    url(r'^friend_cancel/(?P<pk>\d+)$', views.friend_cancel, name="friend_cancel"),
]