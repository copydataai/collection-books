"""Views books"""

# DRF
from rest_framework import viewsets, mixins

# models
from collection_books.books.models import Book

# Serializers
from collection_books.books.api.serializers import BookModelSerializer


class BookViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """Book view set"""

    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
