from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']
    ordering = ['email']
    search_fields = ['email', 'username']
    fieldsets = BaseUserAdmin.fieldsets
    add_fieldsets = BaseUserAdmin.add_fieldsets

admin.site.register(User, UserAdmin)
