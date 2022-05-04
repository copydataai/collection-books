

# DRF
from rest_framework import mixins, viewsets

# model
from collection_books.categories.models import Category

# serializer
from collection_books.categories.api.serializers import CategoryModelSerializer


class CategoryViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """"""

    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
