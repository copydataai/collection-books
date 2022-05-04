"""Views narrators"""

# DRF
from rest_framework import viewsets, mixins

# models
from collection_books.narrators.models import Narrator

# Serializers
from collection_books.narrators.api.serializers import NarratorModelSerializer

class NarratorViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """Narrator view set"""

    serializer_class = NarratorModelSerializer
    queryset = Narrator.objects.all()
