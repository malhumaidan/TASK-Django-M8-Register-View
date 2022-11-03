from datetime import timedelta, datetime
from rest_framework.permissions import BasePermission
from django.utils import timezone


class IsOwner(BasePermission):
    message = "This is not your booking"

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.owner == request.user

class ThreeDaysRule(BasePermission):
    message = "Cannot be canceled or modified"

    def has_object_permission(self, request, view, obj):
        delta = timedelta(days=3)
        date = datetime.today().date()
        final = date + delta
        return obj.date > final
