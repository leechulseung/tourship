from django.contrib import admin
from .models import Post, Comment , Postprivacy

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Postprivacy)
class PostprivacyAdmin(admin.ModelAdmin):
    pass
