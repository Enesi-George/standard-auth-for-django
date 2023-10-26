from rest_framework import serializers
from .models import DimensionPrice
class DimensionPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimensionPrice
        fields = ('id', 'storage_type', 'dimension', 'price')