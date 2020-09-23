from django.db import models
from blog.models import Article

# Create your models here.

# '''


class Comment(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, default='游客')
    email = models.EmailField(max_length=100, default='xxxxx@example.com')
    content = models.TextField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    # test = models.IntegerField(default=1)
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]

    class Meta:
        # order_with_respect_to = 'created_time'
        ordering = ['-created_time']
