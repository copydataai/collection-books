"""Narrator admin conf"""

# Django
from django.contrib import admin

# models
from collection_books.narrators.models import Narrator

admin.site.register(Narrator)
