from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import IsAdmin


class RegisterView(generics.CreateAPIView):
    """
    Call -> POST /api/auth/register/
    it creates a new user
    """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Call -> POST /api/auth/login/
    it returns JWT tokens
    """
    permission_classes = (permissions.AllowAny,)