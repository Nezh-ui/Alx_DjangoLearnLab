from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (None, {'fields': ('date_of_birth', 'profile_picture')})

    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {'fields': ('date_of_birth', 'profile_picture')}),
    )
    

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib.auth.decorators import user_passes_test