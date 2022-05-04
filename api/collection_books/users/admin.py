"""User models admin"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from collection_books.users.models.user import User


class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ["email", "username", "first_name", "last_name", "is_client"]
    list_filter = ['is_client', 'is_staff', 'created', 'modified']


admin.site.register(User, CustomUserAdmin)
