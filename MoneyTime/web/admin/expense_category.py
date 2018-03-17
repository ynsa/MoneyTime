from django.contrib import admin

from MoneyTime.web.models import ExpenseCategory


class ExpenseCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user']
    list_display = ['name', 'user']


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
