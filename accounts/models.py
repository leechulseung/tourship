from django.db import models
from django.conf import settings
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Local(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    country = models.ForeignKey('Country')
    local = models.ForeignKey('Local')
    address = models.CharField('상세주소',max_length= 50)
    birthdate = models.CharField('생일',max_length= 120, blank=True)
    gender = models.CharField('성별',max_length=5)
    phone_num = models.CharField('전화번호',max_length=15)
    is_certified = models.BooleanField('인증여부', blank=True, default=False)
    is_certified_time = models.DateTimeField('인증시간', blank=True)
    def __str__(self):
        return self.user.username

class Timechecking(models.Model):
    profile = models.OneToOneField(Profile)
    time = models.DateTimeField('시간', blank=True)
    token = models.CharField('토큰', max_length=10)