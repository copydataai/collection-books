"""Serializers"""

# Type Static
from typing import Dict, List

# Django
from django.contrib.auth import get_user_model

# DRF
from rest_framework import serializers

# Models
from collection_books.users.models.profile import Profile
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: List = [
            "username",
            "first_name",
            "url",
            "email",
            "is_client",
            "is_verified",
            ]

        extra_kwargs: Dict = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields: List = [
            "biography",
            "picture",
            "biography",
            ]
