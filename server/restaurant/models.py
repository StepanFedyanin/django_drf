from django.db import models
from django.conf import settings
import datetime


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/dish')

    def __str__(self):
        return self.name


class DishCategory(models.Model):
    category = models.CharField(max_length=255)
    dish = models.ManyToManyField(Dish, null=True)

    def __str__(self):
        return self.category


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dishCategory = models.ManyToManyField(DishCategory, null=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.dish.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False, null=True)
    status = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_dish = models.ManyToManyField(OrderItem, null=True)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant.name

    def accept_order(self):
        self.status = False
        self.date = datetime.datetime.now()
        self.save()
        return self

