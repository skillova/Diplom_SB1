import secrets
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from config.settings import EMAIL_HOST_USER
from .models import User
from .serializers import UserSerializer, ResetPasswordRequestSerializer, ResetPasswordSerializer


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


class RequestPasswordReset(generics.GenericAPIView):
    """
    Генератор ссылки сброса пароля на электронную почту
    - POST
    {"email":"почта"}
    """
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token = secrets.token_hex(20)
            user.token = token
            user.save()
            host = request.get_host()
            reset_url = f"http://{host}/{user.pk}/{token}"
            # Sending reset link via email (commented out for clarity)
            send_mail(
                subject='Подтверждение почты',
                message=f'Подтвердите вашу регистрацию перейдя по ссылке {reset_url}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return Response({'success': 'На Вашу почту отправлена ссылка для сброса пароля'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Пользователь с такой почтой не найден"}, status=status.HTTP_404_NOT_FOUND)


class ResetPassword(generics.GenericAPIView):
    """
    Установка нового пароля пользователю
    - POST
    {"uid": "<pk>", "token": "<token>", "new_password": "<new_password>"}
    """
    serializer_class = ResetPasswordSerializer
    permission_classes = []

    def post(self, request):
        token = request.data['token']
        reset_obj = User.objects.filter(token=token).first()
        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)
        pk = request.data['uid']
        user = User.objects.filter(pk=pk).first()
        if user:
            new_password = request.data['new_password']
            user.set_password(new_password)
            user.save()
            return Response({'success': 'Пароль обновлен'})
        else:
            return Response({'error': 'Пользователь не найден'}, status=404)
