# Python
from typing import Optional

# Django
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import QuerySet


class BookManager(models.Manager):
    """Manager for books."""

    def get_if_exist(self, id: str) -> Optional['Book']:
        try:
            return self.get(id=id)
        except:
            return None
        
    def get_queryset(self) -> QuerySet['Book']:
        return BookQuerySet(
            model=Book,
            using=self._db
        )
        

class BookQuerySet(models.QuerySet):
    """QuesHahahahahah."""

    def get_if_exist(self, id: str) -> Optional['Book']:
        try:
            return self.get(id=id)
        except:
            return None


class Book(models.Model):
    """Book for temp project."""

    title = models.CharField(
        verbose_name="book",
        max_length=200
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    desription = models.TextField(
        verbose_name="description"
    )
    price = models.DecimalField(
        verbose_name="price",
        max_digits=10,
        decimal_places=2
    )
    objects = BookManager()

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return f"{self.title} | {self.author.first_name} | {self.price}"

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if (
            self.price <= 0
        ) and {
            not self.price
        }:
            raise ValidationError(
                "Price lte zero!"
            )

        return super().clean()
