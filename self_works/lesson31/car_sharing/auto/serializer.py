from rest_framework import serializers
from .models import Auto, ModelAuto, BrandAuto


class AutoSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()

    class Meta:
        model = Auto
        fields = ('vin_number', 'model', 'brand', 'mileage')


class ModelSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = ModelAuto
        fields = ('name', 'brand')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandAuto
        fields = ('name',)
