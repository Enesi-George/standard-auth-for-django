from django.db import models
from physical_storage.models import PhysicalStorage

class DimensionPrice(models.Model):
    storage_type= models.ForeignKey(PhysicalStorage, on_delete=models.CASCADE)
    dimension= models.CharField(max_length=500)
    price= models.CharField(max_length=30)

    def __str__(self):
        return f"Dimension: {self.dimension}, Price: {self.price}"