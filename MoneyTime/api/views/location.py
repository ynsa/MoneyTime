# 3rd party
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from MoneyTime.api.serializers import LocationSerializer
from MoneyTime.web.models import Location


class LocationViewSet(viewsets.ModelViewSet):
        """ViewSet for the Location Model"""

        queryset = Location.objects.all()
        serializer_class = LocationSerializer
        # filter_class = TransactionFilter
        permission_classes = [permissions.IsAuthenticated]
        filter_backends = (
            filters.SearchFilter,
            filters.OrderingFilter,
            DjangoFilterBackend,
        )
