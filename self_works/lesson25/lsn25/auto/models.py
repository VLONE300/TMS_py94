from django.db import models


# Create your models here.
class Auto(models.Model):
    vin_number = models.CharField(max_length=255)
    model = models.ForeignKey('ModelAuto', on_delete=models.CASCADE)
    status_rent = models.BooleanField(default=False)
    brand = models.ForeignKey("BrandAuto", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.vin_number}'


class ModelAuto(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('BrandAuto', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class BrandAuto(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f'{self.name}'


class UserAuto(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    auto = models.ForeignKey('Auto', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    models = models.ForeignKey('ModelAuto', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name}'
