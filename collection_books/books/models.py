"""Books model"""

# Django
from django.db import models

# Utils
from collection_books.utils.models import CBooksModel

# models
from collection_books.authors.models import Author
from collection_books.narrators.models import Narrator
from collection_books.categories.models import Category


class Book(CBooksModel):
    """Book model"""

    title: models.CharField = models.CharField(
        'title of the book',
        max_length=200
    )

    description: models.TextField = models.TextField(
        'description of the book',
        max_length=500
    )

    book_cover: models.ImageField = models.ImageField(
        'book cover of the book',
        upload_to='books/covers/',
        blank=True,
        null=True
    )

    author: models.ForeignKey = models.ForeignKey(
        Author,
        null=True,
        on_delete=models.SET_NULL,
    )
    narrator: models.ForeignKey = models.ForeignKey(
        Narrator,
        null=True,
        on_delete=models.SET_NULL,
    )

    book: models.FileField = models.FileField(
        'book file',
        upload_to='books/book/',
        blank=True,
        null=True
    )

    categories: models.ManyToManyField = models.ManyToManyField(
        Category,
    )

    class Meta:
        """Meta option
        add ordering
        """
        ordering = ['title']
