from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^joinus/$', views.joinus, name="joinus"),
    url(r'^index/$', views.index ,name="index"),
    url(r'^set_up/$', views.set_up, name="set_up"),
    url(r'^sign_out/$', views.sign_out, name="sign_out"),
]