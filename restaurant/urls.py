
from rest_framework import routers
from restaurant import views


router = routers.DefaultRouter()

router.register(r'restaurant', views.RestaurantViewSet, basename='restaurant')
