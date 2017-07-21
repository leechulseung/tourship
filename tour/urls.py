"""tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from accounts.views import login
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^newspeed/', include('news.urls', namespace="news")),
    url(r'^group/', include('group.urls', namespace='group')),
]

urlpatterns += [
    url(r'^$', login, name='login'),
    
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page':settings.LOGIN_URL})
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)