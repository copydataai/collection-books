"""Views narrators"""

# DRF
from rest_framework import viewsets, mixins

# models
from collection_books.authors.models import Author

# Serializers
from collection_books.authors.api.serializers import AuthorModelSerializer

class AuthorViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """Author view set"""

    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()
