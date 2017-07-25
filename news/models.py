from django.db import models
from django.conf import settings
from accounts.models import Country, Local
from django import forms

class Post(models.Model):
    title = models.CharField('제목',max_length=128)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=' user related',
        related_name='%(app_label)s_%(class)ss') 
    photo = models.ImageField('사진', blank=True, upload_to='newspeed/%Y/%m/%d/')
    content = models.TextField('내용',)
    country = models.ForeignKey(Country, verbose_name='국가',
        related_name="%(app_label)s_%(class)ss")
    local = models.ForeignKey(Local,verbose_name='지역',
        related_name='%(app_label)s_%(class)ss')
    address = models.TextField('상세주소')
    tourdate = models.CharField('여행날짜',max_length=15)
    privacy = models.ForeignKey('Postprivacy',verbose_name='Privacy related',
        related_name='%(app_label)s_%(class)ss')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at =models.DateTimeField('수정일', auto_now=True)

    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like') # post.like_set 으로 접근 가능
    
    def get_absolute_url(self):
        return reverse('news:news_list', args=[self.id])

    def delete(self, *args, **kwargs):  
        self.photo.delete()
        super(Post, self).delete(*args, **kwargs)

    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.author.username
        
class Postprivacy(models.Model):
    policy = models.CharField('정책',max_length=15)

    def __str__(self):
        return self.policy

class Comment(models.Model):
    post = models.ForeignKey('Post', verbose_name='post related',
        related_name='%(app_label)s_%(class)ss'
        )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=' user related',
        related_name='%(app_label)s_%(class)ss')
    message = models.TextField('댓글')
    created_at = models.DateTimeField('작성일',auto_now_add=True)
    updated_at =models.DateTimeField('수정일', auto_now=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets={
        'message': forms.TextInput(attrs={
        'class':'form-control mb-2 mr-sm-2 mb-sm-0 reply_text',
        'placeholder':'댓글을 입력해주세요.',    
            })
        }

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
