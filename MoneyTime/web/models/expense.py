# django
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from MoneyTime.settings import AUTH_USER_MODEL
from MoneyTime.web.models import ExpenseCategory, Location


class Expense(models.Model):
    """Model Expense."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='expense',
        verbose_name=_('User')
    )

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='expense_category',
        verbose_name=_('Category')
    )

    amount = models.DecimalField(
        _('Amount'),
        default=0,
        max_digits=16,
        decimal_places=8,
    )

    # currency = models.ForeignKey(
    #     Currency,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='expense_currency',
    #     verbose_name=_('Currency')
    # )

    created = models.DateTimeField(_('Created'), auto_now_add=True)

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='expense',
        verbose_name=_('Location')
    )

    # location = models.PointField(_('Where spent money'), null=True, blank=True)

    creation_location = models.PointField(
        _('Where create expense'),
        null=True,
        blank=True
    )

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.pk, self.category, self.created)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
