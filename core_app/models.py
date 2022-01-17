from django.db import models
from .consts import CATEGORY_TYPE


class Category(models.Model):
    title = models.CharField(
        max_length=24,
        choices=CATEGORY_TYPE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'
