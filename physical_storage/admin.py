from django.contrib import admin
from .models import PhysicalStorage
from .dimension_price.models import DimensionPrice
from .customer_form.models import PhyscialStorageForm

# Register your models here.
@admin.register(PhysicalStorage)
class PhysicalStorageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PhysicalStorage._meta.fields]

@admin.register(DimensionPrice)
class DimensionPriceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DimensionPrice._meta.fields]    

@admin.register(PhyscialStorageForm)
class CustomerFormAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PhyscialStorageForm._meta.fields]     

@admin.register(DimensionPriceAdmin)
class CustomerFormAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PhyscialStorageForm._meta.fields]      