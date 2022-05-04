"""Narrator model"""

# Django
from django.db import models

class Narrator(models.Model):
    """Narrator model"""
    first_name: models.CharField = models.CharField(max_length=100)
    last_name: models.CharField = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']
