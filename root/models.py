from django.db import models


class Base(models.Model):
    """ Abstract model to save the common data """
    timestamp = models.DateTimeField(auto_now_add=True)
    year = models.PositiveIntegerField(default=2018)

    class Meta:
        abstract = True
