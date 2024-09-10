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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={
            'invalid': (
                'Password must be at least 8 characters long with at least one capital letter and symbol'
            )
        }
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
