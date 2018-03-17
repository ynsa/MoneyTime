from django.db import models
from django.utils.translation import ugettext_lazy as _

from MoneyTime.settings import AUTH_USER_MODEL


class ExpenseCategory(models.Model):
    """Model ExpenseCategory."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='expense_category',
        verbose_name=_('User')
    )
    name = models.CharField(_('Name'), max_length=64)

    def __str__(self):
        return '{0}'.format(_(self.name))

    class Meta:
        ordering = ['user__email']
        verbose_name = _('Expense category')
        verbose_name_plural = _('Expense categories')
