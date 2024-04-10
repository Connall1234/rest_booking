from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define a custom UserAdmin class
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
