from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length= 50)
    birthdate = models.CharField(max_length= 120, blank=True)
    gender = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=15)