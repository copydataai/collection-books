"""Profile model"""

# Django
from django.db import models

# Utils
from collection_books.utils.models import CBooksModel


class Profile(CBooksModel):
    """Profile model"""

    user: models.OneToOneField = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE
        )
    picture: models.ImageField = models.ImageField(
        'profile picture',
        upload_to='users/picture/',
        blank=True,
        null=True
    )

    biography: models.TextField = models.TextField(
        max_length=500,
        blank=True
        )
