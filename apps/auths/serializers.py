# Python
from collections import OrderedDict
from typing import Any

# Django
from django.contrib.auth.hashers import make_password

# DRF
from rest_framework import serializers

# Thir-party Apps
from banks.serializers import User


class LoginSerializer(serializers.ModelSerializer):
    """Login."""

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class RegisterSerializer(serializers.ModelSerializer):
    """Register."""

    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password2',
        )

    def validate(
        self, 
        attrs: OrderedDict
    ) -> Any:
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                "пароли не совпадают"
            )
        
        return super().validate(attrs)

    def save(self, **kwargs):
        user = User.objects.create(
            username=self.data.get('username'),
            email=self.data.get('email'),
            password=make_password(
                self.data.get('password')
            )
        )

        return user
