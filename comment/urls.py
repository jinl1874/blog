from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    url(r'^comment/article/(?P<article_id>[0-9]+)/$',
        views.art_comment, name='art_comment')
]
