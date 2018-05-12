# 3rd party
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from MoneyTime.api.serializers.location_category import \
    LocationCategorySerializer
from MoneyTime.web.models import LocationCategory


class LocationCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the LocationCategory Model"""

    serializer_class = LocationCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )

    def get_queryset(self):
        user = self.request.user
        return LocationCategory.objects.filter(user=user)
