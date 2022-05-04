"""Serializers books"""

# Typing
from typing import List

# DRF
from rest_framework.serializers import ModelSerializer

# models
from collection_books.books.models import Book


class BookModelSerializer(ModelSerializer):
    """Book model serializer"""
    class Meta:
        model = Book
        fields: List = ['title',
                        'description',
                        'book_cover',
                        'author',
                        'book',
                        'narrator',
                        'categories']
