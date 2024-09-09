from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


from .apps import UsersConfig
from .views import CreateUserView, ResetPassword

app_name = UsersConfig.name

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uid>/<token>/', PasswordResetConfirmView.as_view(), name='password_confirm'),
    path("reset_password", ResetPassword.as_view()),
]
