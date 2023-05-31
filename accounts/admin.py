from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'age', 'is_staff']
    fieldsets = (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('age',)}),
    )
