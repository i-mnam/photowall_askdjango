from django.contrib import admin
from .models import Post, Comment

@admin.register(Post) # admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'created_at']
    list_display_links = ['title']
    list_editable = ['is_public']

admin.site.register(Comment)