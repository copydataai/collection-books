"""Author admin"""

# Django
from django.contrib import admin

# models
from collection_books.authors.models import Author


admin.site.register(Author)
