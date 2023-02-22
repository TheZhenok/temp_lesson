# Python
from django.contrib.auth.models import User

# DRF
from rest_framework import serializers

# Local
from .models import Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Book serializer."""

    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

