from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

NULLABLE = {
    'null': True,
    'blank': True
}


class UserRoles(models.TextChoices):
    """
    Роли пользователя:
    user - может получать список объявлений, получать одно объявление, создавать объявление,
    редактировать и удалять свое объявление, получать список комментариев, создавать комментарии,
    редактировать/удалять свои комментарии.
    admin - может дополнительно к правам пользователя редактировать или удалять объявления и
    комментарии любых других пользователей.
    """

    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    """
    Модель пользователя наследуется от модели AbstractUser.
    / AbstractUser — это абстрактная модель, которая предоставляет полную реализацию модели пользователя по умолчанию.
    / USERNAME_FIELD – уникальный идентификатор пользователя. Это поле, вместе с паролем, используется при авторизации.
    / REQUIRED_FIELDS – список полей, которые потребуется ввести при создании пользователя через команду
    createsuperuser. Также этот список нередко используется сторонними библиотеками, при создании формы с регистрацией.
    Нормальная форма с регистрацией включает в себя: USERNAME_FIELD, REQUIRED_FIELDS и password.
    / is_active – активен ли пользователь или нет (default: False).
    / is_staff – имеет ли пользователь доступ к панели администратора или нет (default: False).
    """

    username = None

    first_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name='имя пользователя',
        help_text='Укажите имя',
    )
    last_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name='фамилия пользователя',
        help_text='Укажите фамилию',
    )
    phone_number = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name='номер телефона',
        help_text='Укажите номер телефона',
    )
    avatar = models.ImageField(
        upload_to='users/',
        **NULLABLE,
        verbose_name='Аватар',
        help_text='Загрузите аватар',
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        help_text='Укажите электронную почту'
    )
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default='user',
        verbose_name='статус пользователя',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} - {self.role}'

    objects = UserManager()

    def save(self, *args, **kwargs):
        if 'pbkdf2_sha256' not in self.password:
            password = make_password(self.password)
            self.password = password
        super().save(*args, **kwargs)
