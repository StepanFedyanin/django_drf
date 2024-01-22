from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    type = models.CharField(max_length=255)
    dishs = models.ManyToManyField(Dish)
