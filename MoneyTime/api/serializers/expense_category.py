# 3rd party
from rest_framework import serializers

from MoneyTime.web.models import ExpenseCategory


class ExpenseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategory
        exclude = []
        # fields = (
        #     'pk',
        #     'name',
        #     'symbol',
        #     'is_crypto',
        #     'price',
        # )
