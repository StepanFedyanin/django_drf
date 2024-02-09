from django.db import models
from django.conf import settings


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


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    def __str__(self):
        return self.restaurant
