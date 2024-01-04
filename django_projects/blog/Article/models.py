from django.db import models
from Author.models import Author


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ManyToManyField(Author)
