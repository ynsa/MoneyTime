# 3rd party
from rest_framework import serializers

from MoneyTime.web.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        exclude = []
        # fields = (
        #     'pk',
        #     'name',
        #     'symbol',
        #     'is_crypto',
        #     'price',
        # )
