from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'telegram', 'avatar', 'is_active', 'is_staff', 'date_joined',)
    ordering = ('id',)
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    'username',
                    'email',
                    'telegram',
                    'avatar',
                    'is_active',
                    'is_staff',
                    'password1',
                    'password2',
                ),
            },
        ),
    )
    fieldsets = [
        (
            None,
            {
                "fields": (
                    'username',
                    'email',
                    'telegram',
                    'avatar',
                    'is_active',
                    'is_staff',
                    'password',
                ),
            },
        ),
    ]