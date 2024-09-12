from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


from .apps import UsersConfig
from .views import CreateUserView, RequestPasswordReset, ResetPassword

app_name = UsersConfig.name

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('reset_password/', RequestPasswordReset.as_view()),
    path('reset_password_confirm/', ResetPassword.as_view()),
]
