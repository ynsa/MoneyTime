# 3rd party
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from MoneyTime.api.serializers import LocationSerializer
from MoneyTime.web.models import Location


class LocationViewSet(viewsets.ModelViewSet):
        """ViewSet for the Location Model"""

        serializer_class = LocationSerializer
        permission_classes = [permissions.IsAuthenticated]
        filter_backends = (
            filters.SearchFilter,
            filters.OrderingFilter,
            DjangoFilterBackend,
        )

        def get_queryset(self):
            user = self.request.user
            return Location.objects.filter(user=user)
