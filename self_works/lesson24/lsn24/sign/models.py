from django.db import models


# Create your models here.
class UserLsn24(models.Model):
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.email