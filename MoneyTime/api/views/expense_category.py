# 3rd party
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from MoneyTime.api.serializers import ExpenseCategorySerializer
from MoneyTime.web.models import ExpenseCategory


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the ExpenseCategory Model"""

    serializer_class = ExpenseCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )

    def get_queryset(self):
        user = self.request.user
        return ExpenseCategory.objects.filter(user=user)
