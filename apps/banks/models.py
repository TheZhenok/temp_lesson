# Python
from datetime import date, timedelta

# Django
from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator

from auths.models import CUser


User: AbstractBaseUser = CUser

class Card(models.Model):
    """Card for user."""

    number = models.CharField(
        verbose_name="номер",
        max_length=16,
        validators=[
            MinLengthValidator(16)
        ],
        unique=True
    )
    date_expiration = models.DateField(
        verbose_name="дата окончания",
        default=(
            date.today() + timedelta(days=365*4)
        )
    )
    owner = models.ForeignKey(
        to=User,
        verbose_name='владелец карты',
        on_delete=models.CASCADE
    )
    cvv = models.CharField(
        verbose_name='cvv',
        max_length=3,
        validators=[
            MinLengthValidator(3)
        ]
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'карта'
        verbose_name_plural = 'карты'
