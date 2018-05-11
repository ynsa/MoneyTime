# 3rd party
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from MoneyTime.api import ExpenseSerializer
from MoneyTime.web.models import Expense


class ExpenseViewSet(viewsets.ModelViewSet):
        """ViewSet for the Expense Model"""

        queryset = Expense.objects.all()
        serializer_class = ExpenseSerializer
        # filter_class = TransactionFilter
        permission_classes = [permissions.IsAuthenticated]
        filter_backends = (
            filters.SearchFilter,
            filters.OrderingFilter,
            DjangoFilterBackend,
        )
