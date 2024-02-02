
from rest_framework import routers
from restaurant import views

app_name = 'restaurant'

router = routers.DefaultRouter()

router.register(r'', views.RestaurantViewSet, basename='restaurant')
# router.register(r'menu', views.MenuViewSet, basename='menu')
# router.register(r'dish', views.DishViewSet, basename='dish')


urlpatterns = router.urls
