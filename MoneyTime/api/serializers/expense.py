# 3rd party
from rest_framework import serializers

from MoneyTime.api.serializers import ExpenseCategorySerializer, LocationSerializer
from MoneyTime.web.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        exclude = [
            'user'
        ]

    def get_category(self, obj):
        return ExpenseCategorySerializer(obj.category).data

    def get_location(self, obj):
        return LocationSerializer(obj.location).data
