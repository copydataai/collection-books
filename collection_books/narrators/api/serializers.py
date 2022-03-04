"""Serializers narrator"""

# Typing
from typing import List

# DRF
from rest_framework.serializers import ModelSerializer

# models
from collection_books.narrators.models import Narrator


class NarratorModelSerializer(ModelSerializer):
    """Narrator model serializer"""
    class Meta:
        model = Narrator
        fields: List = ['first_name', 'last_name']
