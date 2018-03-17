from django.contrib import admin

from MoneyTime.web.models import LocationCategory


class LocationCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user']
    list_display = ['name', 'user']


admin.site.register(LocationCategory, LocationCategoryAdmin)
