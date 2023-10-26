from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, response
from .serializers import PhysicalStorage, PhysicalStorageSerializer
from django.shortcuts import get_object_or_404
from .dimension_price.views import DimensionPriceViewSet
from .customer_form.views import PhysicalStorageFormViewSet

# Create your views here.

class PhysicalStorageViewSet(viewsets.ViewSet,
                       generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin):
    
    queryset = PhysicalStorage.objects.all()
    serializer_class = PhysicalStorageSerializer

   
