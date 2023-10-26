from rest_framework import serializers
from .models import PhyscialStorageForm

class PhyscialStorageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhyscialStorageForm
        fields = (
            'storage_id',
            'userid',
            'name_of_item',
            'list_of_items',
            'description_of_item', 
            'image',
            'value_of_item_in_naira',
            'dimension_of_storage_with_price',
            'storage_duration_in_month',
            'timestamp'
        )