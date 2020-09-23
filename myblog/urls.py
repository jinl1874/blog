"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('', include('comment.urls')),
    # path(r'hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 设置静态文件路径
    url(r'^static/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.STATIC_ROOT},
        name='static'
        ),
    url(r'^static/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    # 关闭debug要加上这个
    url(r'^media/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.MEDIA_ROOT}, name='media'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 设置媒体路径
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
