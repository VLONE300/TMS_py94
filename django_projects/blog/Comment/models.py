from django.db import models
from Article.models import Article


# Create your models here.
class Comment(models.Model):
    nickname = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
