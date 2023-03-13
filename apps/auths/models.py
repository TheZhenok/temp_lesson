# Python
from typing import (
    Optional,
    Iterable
)
import random

# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError


class CUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'CUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CUser':

        custom_user: 'CUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return

    def create_test_user(self) -> 'CUser':

        custom_user: 'CUser' = self.model(
            email=self.normalize_email('root2@gmail.com'),
            password='qwerty'
        )
        custom_user.set_password('qwerty')
        custom_user.save(using=self._db)
        return custom_user


class CUser(
    AbstractBaseUser, 
    PermissionsMixin
):
    """My custom user."""

    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    first_name = models.CharField(
        verbose_name='firstname',
        max_length=60,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='lastname',
        max_length=70,
        null=True,
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='active',
        default=False
    )
    count_requests = models.PositiveSmallIntegerField(
        verbose_name='кол-во запросов',
        default=10
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CUserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)