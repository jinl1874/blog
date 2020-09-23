from django.contrib import admin
from comment import models

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'created_time')
    search_fields = ('name', 'content',)
    list_filter = ('created_time', 'article')
    ordering = ('-created_time',)
    list_per_page = 10


admin.site.register(models.Comment, CommentAdmin)
