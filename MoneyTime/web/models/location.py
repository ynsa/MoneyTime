# django
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from MoneyTime.settings import AUTH_USER_MODEL
from MoneyTime.web.models import LocationCategory


class Location(models.Model):
    """Model Location."""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='location',
        verbose_name=_('User')
    )

    category = models.ForeignKey(
        LocationCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='location',
        verbose_name=_('Category')
    )

    name = models.CharField(_('Name'), null=True, blank=True, max_length=255)

    location = models.PointField(_('Location'), null=True, blank=True)

    def __str__(self):
        return '{0}({1})'.format(self.name, self.category)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
