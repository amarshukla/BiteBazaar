from rest_framework import serializers
from food.models import Food, Cart, CartItem, Order, OrderItem

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'price')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'food', 'quantity')

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'food', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'items', 'created_at')
