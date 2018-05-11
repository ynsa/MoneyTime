# 3rd party
from django_filters import rest_framework as filters

from MoneyTime.web.models import Expense


class ExpenseFilter(filters.FilterSet):

    class Meta:
        model = Expense
        fields = (
            'user',
            'location',
        )
