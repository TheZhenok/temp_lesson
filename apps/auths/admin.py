# Python
from typing import (
    Any,
    Optional
)

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest

# Local
from .models import CUser


class CUserAdmin(UserAdmin):

    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'password',
                'count_requests'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )
    # NOTE: Used to define the fields that
    #       will be displayed on the create-user page
    #
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active'
            ),
        }),
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'is_superuser',
        'is_staff',
        'is_active'
    )
    list_display = (
        'email',
        'password',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    list_filter = (
        'email',
        'is_superuser',
        'is_staff',
        'is_active'
    )
    ordering = (
        'email',
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[CUser] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'email',
        )

    def has_add_permission(self, request: WSGIRequest) -> bool:
        return True

    def has_change_permission(
        self,
        request: WSGIRequest,
        obj: Any = None
    ) -> bool:
        return True

    def has_delete_permission(
        self,
        request: WSGIRequest,
        obj: Any = None
    ) -> bool:
        return True


admin.site.register(CUser, CUserAdmin)