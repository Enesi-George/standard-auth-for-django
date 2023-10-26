from rest_framework import routers
from .views import PhysicalStorageViewSet, DimensionPriceViewSet, PhysicalStorageFormViewSet


router = routers.DefaultRouter()

#Physical Storage Endpoint
router.register(r'price',DimensionPriceViewSet, basename="delivery_price")

router.register(r'customer_form',PhysicalStorageFormViewSet, basename="customer_form")



router.register(r'', PhysicalStorageViewSet, basename="physical-storage")


urlpatterns = router.urls