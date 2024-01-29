from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/dish')

    def __str__(self):
        return self.name


class Menu(models.Model):
    type = models.CharField(max_length=255)
    dish = models.ManyToManyField(Dish)

    def __str__(self):
        return self.type


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    menus = models.ManyToManyField(Menu, null=True)

    def __str__(self):
        return self.name