from rest_framework import serializers
from .models import Vinyl, Order, OrderItem
from datetime import datetime

class VinylSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinyl
        fields = '__all__'
        
    def validate_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("El año no puede ser en el futuro.")
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate(self, data):
        vinyl = data['vinyl']
        quantity = data['quantity']
        if vinyl.stock < quantity:
            raise serializers.ValidationError(
                f"Stock insuficiente para el disco '{vinyl.title}'. Solo quedan {vinyl.stock} unidades."
            )
        return data

    def create(self, validated_data):
        vinyl = validated_data['vinyl']
        quantity = validated_data['quantity']
        # Descontar el stock automáticamente
        vinyl.stock -= quantity
        vinyl.save()
        return super().create(validated_data)

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
