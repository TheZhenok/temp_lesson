# Python
from typing import Optional

# Django
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

# Local
from .models import Book


class BookAdmin(admin.ModelAdmin):
    """Book admin."""

    model = Book
    list_display = [
        'title',
        'price',
    ]
    readonly_fields = (

    )

    def get_readonly_fields(
        self, 
        request: WSGIRequest, 
        obj: Optional[Book]
    ) -> tuple:
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'price',
        )

admin.site.register(Book, BookAdmin)
