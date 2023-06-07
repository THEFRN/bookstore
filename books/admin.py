from django.contrib import admin

from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_time_created', 'book', 'text', 'is_active', 'recommend']


admin.site.register(Book)
