"""Books App"""

# Django
from django.apps.config import AppConfig


class BooksConfig(AppConfig):
    """Books app config"""
    name: str = 'collection_books.books'
    verbose_name: str = 'books'
