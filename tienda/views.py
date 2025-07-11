from rest_framework import viewsets
from .models import Vinyl, Order, OrderItem
from .serializers import VinylSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS

# Permiso personalizado para Vinyl
class VinylPermission(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class VinylViewSet(viewsets.ModelViewSet):
    queryset = Vinyl.objects.all()
    serializer_class = VinylSerializer
    permission_classes = [VinylPermission]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
