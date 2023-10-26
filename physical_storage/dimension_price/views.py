from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from .serializers import DimensionPrice, DimensionPriceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.

class DimensionPriceViewSet(viewsets.ModelViewSet):
    queryset = DimensionPrice.objects.all()
    serializer_class = DimensionPriceSerializer