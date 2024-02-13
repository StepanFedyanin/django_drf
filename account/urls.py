from rest_framework import routers
from account import views

router = routers.DefaultRouter()

router.register(r'', views.AccountViewSet, basename='users')
router.register(r'login', views.LoginWithPhoneViewSet, basename='users')

app_name = 'account'
urlpatterns = router.urls