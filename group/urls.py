from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.group_index , name="group_index"),
    url(r'^make/$', views.group_make, name="group_make"),
    url(r'^group_book/$', views.group_book, name='group_book'),
]