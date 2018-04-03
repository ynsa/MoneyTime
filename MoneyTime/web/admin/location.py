from django.contrib.gis import admin

from MoneyTime.web.models.location import Location


class LocationAdmin(admin.OSMGeoAdmin):
    search_fields = ['category', 'user']
    list_display = ['name', 'category', 'user']


admin.site.register(Location, LocationAdmin)
