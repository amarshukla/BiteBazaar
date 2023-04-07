
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from accounts.permissions import IsCreationOrIsAuthenticated
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)