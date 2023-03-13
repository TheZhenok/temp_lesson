# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

# DRF
from rest_framework import serializers

# Local
from .models import Card

from auths.models import CUser


User: AbstractBaseUser = CUser

class UserSerializer(serializers.ModelSerializer):
    """User."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name'
        )
        

class CardSerializer(serializers.ModelSerializer):
    """Card serializer."""

    owner = UserSerializer()

    class Meta:
        model = Card
        fields = '__all__'
