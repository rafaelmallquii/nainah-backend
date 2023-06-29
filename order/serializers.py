from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(read_only=True)
    products = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'