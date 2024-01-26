from django.db import models


# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='cat_news/images/', blank=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comments = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    nick_name = models.CharField(max_length=128)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.nick_name} on {self.date}'

