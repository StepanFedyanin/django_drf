from django.contrib import admin

from restaurant.models import Restaurant, Menu,Dish

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Dish)