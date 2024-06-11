from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'likes')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_date', 'author')
    date_hierarchy = 'created_date'

