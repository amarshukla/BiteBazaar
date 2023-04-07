from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from food.models import Food, Cart, CartItem, Order, OrderItem
from food.serializers import FoodSerializer, CartSerializer, OrderSerializer
from accounts.permissions import IsCreationOrIsAuthenticated
from rest_framework.authentication import TokenAuthentication

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)
    

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsCreationOrIsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def add_food(self, request):
        food_id = request.data.get('food_id')
        quantity = request.data.get('quantity', 1)

        food = Food.objects.get(id=food_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def place_order(self, request):
        cart = Cart.objects.filter(user=request.user).first()

        if not cart:
            return Response({'error': 'Cart is empty'}, status=400)

        order = Order.objects.create(user=request.user)

        for cart_item in cart.items.all():
            OrderItem.objects.create(order=order, food=cart_item.food, quantity=cart_item.quantity)

        cart.items.all().delete()
        cart.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsCreationOrIsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
