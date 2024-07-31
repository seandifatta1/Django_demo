from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_auth.forms import CustomUserCreationForm, CustomUserChangeForm
from djangoProject2.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'favorite_team', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'favorite_team')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'favorite_team', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
