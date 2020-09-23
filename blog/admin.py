from django.contrib import admin
from blog.models import Article, Category, Author
# Register your models here.


class AritcleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'pub_time', 'cate_name')
    search_fields = ('title', 'summary', 'content')
    list_filter = ('pub_time', 'cate_name')
    # 只针对多对多
    filter_horizontal = ('author',)
    # 针对外键
    raw_id_fields = ('cate_name',)
    # 让每页显示几条记录的设置
    list_per_page = 10
    list_editable = ('cate_name',)
    # 排序
    ordering = ('-pub_time', )
    date_hierarchy = 'pub_time'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, AritcleAdmin)
admin.site.register(Category, CategoryAdmin)
