from django.http import JsonResponse
from rest_framework import generics

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, ResetPasswordSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Создание нового пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class ResetPasswordUsers(APIView):
    """
    Класс для обновления пароля
    """

    permission_classes = (IsAuthenticated,)

    pass
