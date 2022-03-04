"""User models admin"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from collection_books.users.models.profile import Profile
from collection_books.users.models.user import User


class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ["email", "username", "first_name", "last_name", "is_client"]
    list_filter = ['is_client', 'is_staff', 'created', 'modified']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name',)


admin.site.register(User, CustomUserAdmin)
