# 3rd party
from rest_framework import serializers

from MoneyTime.web.models import LocationCategory


class LocationCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationCategory
        exclude = []
        # fields = (
        #     'pk',
        #     'name',
        #     'symbol',
        #     'is_crypto',
        #     'price',
        # )
