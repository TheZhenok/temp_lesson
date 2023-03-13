# Django
from django.db.models.query import QuerySet

from .models import CUser


def re_zero_counts_service():
    users: QuerySet[CUser] = CUser.objects.all()
    users.update(count_requests=10)

