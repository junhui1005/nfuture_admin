from django.contrib import admin
from .models import Member, Post

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined_at')
    search_fields = ('name', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author',)
    search_fields = ('title',)
