# Python
from typing import (
    Union,
    TypeAlias
)

# Django
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.views import View  # return html

# DRF
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request

# Local
from .models import Book
from .serializers import BookSerializer


class BookView(ViewSet):
    """Book view."""

    queryset: QuerySet[Book] = Book.objects.all()
    serializer: TypeAlias = BookSerializer

    def list(
        self,
        request: Request,
        *args,
        **kwargs
    ) -> Response:
        result: BookSerializer = self.serializer(
            self.queryset,
            many=True
        )
        return Response(
            data=result.data,
            status=200
        )
    
    def retrieve(
        self,
        request: Request,
        pk: str,
        *args,
        **kwargs  
    ) -> Response:
        
        book: Book = self.queryset.get_if_exist(id=pk)
        if not book:
            return Response({
                "error": f"Book {pk} not found"
            }, status=401)
        
        result: BookSerializer = self.serializer(
            book
        )

        return Response(
            data=result.data,
            status=200
        )
