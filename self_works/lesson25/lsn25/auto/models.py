from django.db import models


# Create your models here.
class Auto(models.Model):
    vin_number = models.CharField(max_length=255)
    model = models.ForeignKey('ModelAuto', on_delete=models.CASCADE)
    status_rent = models.BooleanField(default=False)
    user = models.ForeignKey('UserAuto', on_delete=models.CASCADE)


class ModelAuto(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('BrandAuto', on_delete=models.CASCADE)


class BrandAuto(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='')


class UserAuto(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
