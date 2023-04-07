from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Food, through='CartItem')

class CartItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Food, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
