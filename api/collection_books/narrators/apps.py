"""Narrator App"""

# Django
from django.apps.config import AppConfig


class NarratorsConfig(AppConfig):
    """Narrator app config"""
    name: str = 'collection_books.narrators'
    verbose_name: str = 'narrators'
