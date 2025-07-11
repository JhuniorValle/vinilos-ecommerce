from rest_framework import routers
from .views import VinylViewSet, OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'vinyls', VinylViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = router.urls
