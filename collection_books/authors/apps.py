"""Author App"""

# Django
from django.apps.config import AppConfig


class AuthorsConfig(AppConfig):
    """Author app config"""
    name: str = 'collection_books.authors'
    verbose_name: str = 'authors'
