from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'email', 'role', 'avatar', 'is_active',
        'is_staff'
    )
    list_display_links = (
        'email',
    )
