# 3rd party
from rest_framework import serializers

from MoneyTime.api.serializers import LocationCategorySerializer
from MoneyTime.web.models import Location


class LocationSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Location
        exclude = [
            'user'
        ]

    def get_category(self, obj):
        return LocationCategorySerializer(obj.category).data
