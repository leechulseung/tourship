from django.contrib import admin
from .models import Profile, Country, Local, Timechecking

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'country_str', 'local_str', 'phone_num']

    def country_str(self, profile):
        return '{}'.format(profile.country.name)

    def local_str(self, profile):
        return '{}'.format(profile.local.name)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

@admin.register(Timechecking)
class TimeCheckingAdmin(admin.ModelAdmin):
    pass
