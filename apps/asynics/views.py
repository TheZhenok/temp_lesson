# Python
from typing import TypeAlias
import asyncio

# Django
from django.shortcuts import render
from django.db.models import QuerySet

# DRF
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
)

# Third party
from banks.models import Card

# Local
from .tasks import check_region

class AsyncViewSet(ViewSet):
    """Test ascync."""

    queryset: QuerySet[Card] = Card.objects.all()

    @action(
        methods=['POST'],
        detail=False,
        url_path='retry'
    )
    def start_async(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        async def main():
            tasks: list[asyncio.Task] = []
            for i in range(13, 23):
                task = asyncio.create_task(
                    check_region(
                        request.data.get('region'),
                        day=i
                    )
                )
                tasks.append(task)

            asyncio.gather(
                *tasks
            )
        
        asyncio.run(main())
        return Response(
            {
                "message": "BAD"
            }, 
            status=204
        )
