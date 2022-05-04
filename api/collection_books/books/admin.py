"""Books admin conf"""

# Django
from django.contrib import admin

# Models
from collection_books.books.models import Book

admin.site.register(Book)
