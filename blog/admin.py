from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('blog_title',)}
    list_filter = ('status', 'created_on')
    list_display = ('blog_title', 'slug', 'status', 'created_on')
    search_fields = ['blog_title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'blog_post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
