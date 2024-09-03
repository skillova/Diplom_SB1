from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создание суперпользователя (администратора)
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.admin',
            first_name='fn_admin',
            last_name='ln_admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role='admin',
        )
        user.set_password('admin')
        user.save()
