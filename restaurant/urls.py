
from rest_framework import routers
from restaurant import views

app_name = 'restaurant'

router = routers.DefaultRouter()

router.register(r'restaurant', views.RestaurantViewSet, basename='restaurant')

urlpatterns = router.urls
