from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv
import os

load_dotenv()


class Command(BaseCommand):
    """
    Создание суперпользователя (администратора)
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('CSU_EMAIL'),
            is_staff=os.getenv('CSU_IS_STAFF'),
            is_superuser=os.getenv('CSU_IS_SUPERUSER'),
            is_active=os.getenv('CSU_IS_ACTIVE'),
            role=os.getenv('CSU_ROLE'),
        )
        password = os.getenv('CSU_PASSWORD')
        user.set_password(password)
        user.save()
