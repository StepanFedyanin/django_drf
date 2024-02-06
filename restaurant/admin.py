from django.contrib import admin

from restaurant.models import Restaurant, Menu, Dish, Order


# Register your models here.
# admin.site.register(Restaurant)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    # list_filter = ('regions', 'publication')
    # list_editable = ('ordering',)


admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(Order)

