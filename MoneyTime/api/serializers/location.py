# 3rd party
from rest_framework import serializers

from MoneyTime.web.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = []
        # fields = (
        #     'pk',
        #     'name',
        #     'symbol',
        #     'is_crypto',
        #     'price',
        # )
