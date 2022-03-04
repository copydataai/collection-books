"""Users app"""

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "collection_books.users"
    verbose_name = "Users"

    # def ready(self):
    #     try:
    #         import collection_books.users.signals  # noqa F401
    #     except ImportError:
    #         pass
