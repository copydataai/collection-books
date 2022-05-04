"""Categories model"""

# Typing
from typing import List

# Django
from django.db import models

class Category(models.Model):
    """Category model"""

    name: models.CharField = models.CharField(max_length=100)

    class Meta:
        ordering: List = ['name']
