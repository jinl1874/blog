from django.urls import re_path, path, include
from django.conf.urls import url
from . import views
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 是大写字母 P
    url(r'^article/(?P<article_id>[0-9]+)/$',
        views.article_page, name='article_detail'),
    re_path(r'^search/$', views.search),
    re_path(r'^category/(?P<cate_name>[a-zA-Z0-9]{1,9})/$', views.category, name='category'),
    url(r'^egg', views.egg, name='egg')
]
