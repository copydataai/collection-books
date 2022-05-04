"""Serializer Categories"""

# Typing
from typing import List

# DRF
from rest_framework import serializers

# model
from collection_books.categories.models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    """Serializer category"""

    class Meta:
        model = Category
        fields: List = ['name']
