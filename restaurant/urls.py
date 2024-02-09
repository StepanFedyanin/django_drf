
from rest_framework import routers
from restaurant import views

app_name = 'restaurant'

router = routers.DefaultRouter()

router.register(r'', views.RestaurantViewSet, basename='restaurant')
# router.register(r'dish', views.DishViewSet, basename='dish')
router.register(r'order', views.OrderViewSet, basename='order')


urlpatterns = router.urls
