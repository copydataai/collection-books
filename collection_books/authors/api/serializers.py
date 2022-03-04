"""Serializers narrator"""

# Typing
from typing import List

# DRF
from rest_framework.serializers import ModelSerializer

# models
from collection_books.authors.models import Author


class AuthorModelSerializer(ModelSerializer):
    """Author model serializer"""
    class Meta:
        model = Author
        fields: List = ['first_name', 'last_name']

