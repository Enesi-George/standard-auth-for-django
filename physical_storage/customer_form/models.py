from django.db import models
from accounts.models import User
from physical_storage.models import PhysicalStorage
from ..dimension_price.models import DimensionPrice
from django.contrib.postgres.fields import ArrayField
# Function to generate a unique file name based on user's first name
def user_upload_path(instance, filename):
    # Get the user's first name and last name
    user_first_name = instance.userid.first_name
    user_last_name = instance.userid.last_name

    # Replace spaces with underscores and make the filename lowercase
    filename = filename.replace(' ', '_').lower()

    # Construct the path
    return f"image_item_of_users/{user_last_name}_{user_first_name}/{filename}"




class PhyscialStorageForm(models.Model):
    
    storage_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_item= models.TextField()
    description_of_item= models.TextField()
    image= models.ImageField(upload_to=user_upload_path,null=True, blank=True)
    value_of_item_in_naira= models.CharField(max_length=30)
    dimension_of_storage_with_price= models.ForeignKey(DimensionPrice, on_delete=models.CASCADE)
    storage_duration_in_month= models.PositiveIntegerField()
    timestamp= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    list_of_items = ArrayField(models.CharField(max_length=1000), default=list)

    def set_list_of_items(self, items):
        self.list_of_items = items

    def get_list_of_items(self):
        return self.list_of_items


    
    def save(self, *args, **kwargs):
        # Check if the storage_id is not set yet (i.e., the object is being created)
        if not self.storage_id:
            # Create a new storage_id by saving the object
            super().save(*args, **kwargs)
        else:
            # The storage_id is already set (i.e., the object is being updated)
            super().save(*args, **kwargs)


    def __str__(self):
        return f"Storage {self.storage_id}"
    
