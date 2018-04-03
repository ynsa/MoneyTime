from django.contrib.gis import admin
from django.utils.translation import ugettext_lazy as _

from MoneyTime.web.models import Expense


class ExpenseAdmin(admin.OSMGeoAdmin):
    list_filter = ['created', ]
    list_display = ['user', 'amount', 'created', 'category', 'location']
    fieldsets = [
        (None, {'fields': ('user',)}),
        (_('Expense'), {'fields': (
            'amount', 'category', 'location', )}),
        (_('Additional information'), {'fields': (
            'creation_location',)}),
    ]


admin.site.register(Expense, ExpenseAdmin)
