from rest_framework import generics
from .models import Auto, ModelAuto, BrandAuto
from .serializer import AutoSerializer, ModelSerializer, BrandSerializer


class AutoListCreate(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class AutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class ModelListCreate(generics.ListCreateAPIView):
    queryset = ModelAuto.objects.all()
    serializer_class = ModelSerializer


class BrandListCreate(generics.ListCreateAPIView):
    queryset = BrandAuto.objects.all()
    serializer_class = BrandSerializer
