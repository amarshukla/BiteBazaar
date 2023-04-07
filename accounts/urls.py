from django.urls import path
from rest_framework import routers
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, basename='users')
urlpatterns = [
    path('auth/', obtain_auth_token),
]
urlpatterns += router.urls