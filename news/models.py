from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField('제목',max_length=128)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=' user related',
        related_name='%(app_label)s_%(class)ss')
    content = models.TextField('내용',)
    photo = models.ImageField('사진', blank=True, upload_to='newspeed/%Y/%m/%d/')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at =models.DateTimeField('수정일', auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('Post', verbose_name='post related',
        related_name='%(app_label)s_%(class)ss'
        )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=' user related',
        related_name='%(app_label)s_%(class)ss')
    message = models.TextField('댓글')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at =models.DateTimeField('수정일', auto_now=True)