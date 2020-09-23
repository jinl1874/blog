# from hitcount.models import HitCount, HitCountMixin
# from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, null=True)
    # arti_num = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=32, default='')
    content = RichTextUploadingField(config_name='my_config')
    author = models.ManyToManyField(Author)
    pub_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    times = models.IntegerField(default=1)
    img_link = models.ImageField(
        upload_to='img/%Y/%m', verbose_name='文件缩略图', default='', null=True)
    cate_name = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, default='摘要: ')
    # hit_count_generic = GenericRelation(
    # HitCount, object_id_field='object_pk',
    # related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail',  kwargs={'article_id': self.id})
