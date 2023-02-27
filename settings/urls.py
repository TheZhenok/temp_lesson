# Django
from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings

# DRF
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Third party apps
from lessons.views import BookView
from banks.views import CardViewSet
from auths.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auths/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

# JWT

urlpatterns += [
    path(
        'api/token/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
]

# DEBUG TOOLBAR

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]

# Routers

router = DefaultRouter(
    trailing_slash=True
)

router.register(
    "books",
    viewset=BookView
)
router.register(
    "banks",
    viewset=CardViewSet
)

urlpatterns += [
    path('api/v1/',include(router.urls)),
]
