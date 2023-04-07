from django.urls import path, include
from rest_framework import routers
from food.views import FoodViewSet, CartViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet, basename='food')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
