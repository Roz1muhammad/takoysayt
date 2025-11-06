

# Register your models here.

from django.contrib import admin
from .models import Post,Comment,User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ("message",)
@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ("username","phone")





