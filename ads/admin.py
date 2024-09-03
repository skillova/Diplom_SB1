from django.contrib import admin

from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description', 'author', 'created_at')
    list_display_links = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'ad', 'created_at')
    list_display_links = ('text',)
