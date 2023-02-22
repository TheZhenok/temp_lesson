# Django
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.db.models import QuerySet

# DRF
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

# Third-Party Apps
from banks.serializers import UserSerializer

# Local
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
)


User = get_user_model()

class RegisterView(APIView):
    """User view."""

    def get(
        self,
        request: Request,
        *args,
        **kwargs
    ) -> Response:
        
        users: QuerySet[User] = User.objects.all()
        serializer: UserSerializer =\
            UserSerializer(
                users, 
                many=True
            )
        
        return Response(
            serializer.data,
            status=200
        )
    
    def post(
        self,
        request: Request,
        *args,
        **kwargs
    ) -> Response:
        
        serializer: LoginSerializer =\
            RegisterSerializer(
                data=request.data
            )
        
        if not serializer.is_valid():
            return Response({
                "error": serializer.error_messages
            })
        
        user: User = serializer.save()
        return Response({
            "message": f"Объект {user.id} создан"
        })
