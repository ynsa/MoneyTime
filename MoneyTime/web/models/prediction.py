from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from MoneyTime.settings import AUTH_USER_MODEL
from MoneyTime.web.models import ExpenseCategory, Location


class Prediction(models.Model):
    """Model Prediction."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='prediction',
        verbose_name=_('User')
    )

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='prediction_expense_category',
        verbose_name=_('Category')
    )

    created = models.DateTimeField(_('Created'), auto_now_add=True)

    predicted = models.DateTimeField(_('Predicted'), blank=True, null=True)

    applied = models.DateTimeField(_('Applied'), blank=True, null=True)

    successful = models.BooleanField(_('Successful'), blank=True, default=False)

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='prediction',
        verbose_name=_('Location')
    )

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.pk, self.category, self.created)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Prediction')
        verbose_name_plural = _('Predictions')
