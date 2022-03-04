"""User model"""
# Typing (implementing static type to python)
from typing import List
# Django
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Utils
from collection_books.utils.models import CBooksModel

class User(CBooksModel, AbstractUser):
    """
    Default custom user model for collection-books-backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    email: EmailField = EmailField('email address', unique=True)

    USERNAME_FIELD: str = 'email'

    REQUIRED_FIELDS: List = ['first_name', 'last_name', 'username']

    is_client: BooleanField = BooleanField(
        'client',
        default=True
    )
    is_verified: BooleanField = BooleanField(
        'verified',
        default=False
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
