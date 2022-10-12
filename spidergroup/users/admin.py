from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


@register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'id', 'email', 'username', 'first_name', 'last_name',
        'is_superuser',
    )
    list_filter = (
        'email', 'username', 'is_superuser',
    )
    fieldsets = (
        ('Общая информация', {'fields': (
            'email', 'username', 'first_name', 'last_name', 'password',
        )}),
        ('Права доступа', {'classes': ('collapse',), 'fields': (
            'is_superuser',
        )})
    )
    add_fieldsets = (
        ('Регистрационные данные', {
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
            )
        }),
        ('Права доступа', {'classes': ('collapse',), 'fields': (
            'is_superuser',
        )})
    )
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    ordering = ('id', 'email', 'username',)