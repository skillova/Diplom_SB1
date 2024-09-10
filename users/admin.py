from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'is_active',
        'is_staff'
    )
    list_display_links = (
        'email',
    )
