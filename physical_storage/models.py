from django.db import models

# Create your models here.
class PhysicalStorage(models.Model):
    storage_type= models.CharField(max_length=255)
    storage_duration = models.IntegerField()
    storage_space= models.CharField(max_length= 255)
    

    @property
    def dimension_price(self):
        from .dimension_price.models import DimensionPrice
        return DimensionPrice.objects.filter(storage_type=self.id).all()
    

    def __str__(self):
        return self.storage_type