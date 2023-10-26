from rest_framework import serializers
from .models import PhysicalStorage
from .dimension_price.serializers import DimensionPriceSerializer

class PhysicalStorageSerializer(serializers.ModelSerializer):
    dimension_price= DimensionPriceSerializer(many= True)

    class Meta:
        model = PhysicalStorage
        fields= '__all__'