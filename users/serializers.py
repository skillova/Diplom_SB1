from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Cериализатор для регистрации пользователя.
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone_number', 'avatar')


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра текущего пользователя.
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'avatar')
