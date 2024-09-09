# from django.contrib.auth.models import BaseUserManager
#
#
# class UserManager(BaseUserManager):
#     """
#     Функция создания пользователя
#     """
#
#     def create_user(self, email, first_name, last_name, phone_number, role='user', password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             phone_number=phone_number,
#             role=role,
#             is_active=True,
#         )
#         user.is_active = True
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, first_name, last_name, phone_number=None, password=None):
#         """
#         Функция создания суперпользователя
#         """
#
#         user = self.create_user(
#             email,
#             first_name=first_name,
#             last_name=last_name,
#             phone_number=phone_number,
#             password=password,
#             role='admin',
#         )
#
#         user.save(using=self._db)
#         return user
