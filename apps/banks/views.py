# Python
from typing import TypeAlias

# Django
from django.shortcuts import render
from django.db.models import QuerySet

# DRF
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
)

# Local
from .models import Card
from .serializers import CardSerializer


class CardViewSet(ViewSet):
    """Viewset for card."""

    queryset: QuerySet[Card] = Card.objects.select_related('owner')
    serializer_class: TypeAlias = CardSerializer
    permission_classes: tuple = (
        IsAuthenticated,
    )

    def list(
        self,
        request: Request,
        *args,
        **kwargs
    ) -> Response:
        
        serializer: CardSerializer = self.serializer_class(
            self.queryset,
            many=True
        )
        return Response(
            serializer.data,
            status=200
        )
