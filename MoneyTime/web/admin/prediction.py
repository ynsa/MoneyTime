from django.contrib.gis import admin
from django.utils.translation import ugettext_lazy as _

from MoneyTime.web.models import Prediction


class PredictionAdmin(admin.OSMGeoAdmin):
    list_filter = ['created', 'successful']
    list_display = ['user', 'applied', 'predicted', 'predicted_delta']
    exclude = []

    def predicted_delta(self, obj):
        if obj.predicted and obj.applied:
            return (
                ' ' + str(obj.predicted - obj.applied) if obj.predicted > obj.applied else '-' + str(
                    obj.applied - obj.predicted))
        return None

    predicted_delta.short_description = 'Delta'


admin.site.register(Prediction, PredictionAdmin)
