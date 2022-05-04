"""Utils models"""

# Django
from django.db.models import Model, DateTimeField


class CBooksModel(Model):
    """Collection Books base model
    CBooksModel acts as an abstract base class from which
    every other model in the project will inherit. This
    class provides every table with the following atributes:
    - created(DateTime)
    - modified(DateTime)
    """
    created: DateTimeField = DateTimeField(
        'created at',
        auto_now_add=True
    )

    modified: DateTimeField = DateTimeField(
        'modified at',
        auto_now=True
    )


    class Meta:
        """Meta option"""
        abstract: bool = True
