from django import forms
from django.contrib import admin
from django.contrib.auth import admin as admin_u
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from MoneyTime.web.models import User

admin.site.site_header = 'MoneyTime'


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)


class UserAdmin(admin_u.UserAdmin):
    search_fields = ['email', 'username',]
    list_filter = ['date_joined', ]
    list_display = ['email', 'username',]
    list_per_page = 25
    fieldsets = [
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Info'), {'fields': (
            'first_name', 'last_name')}),
        (_('Permissions'), {'fields': (
            'is_superuser', 'is_staff', 'is_active',)}),
        (_('Important dates'), {'fields': (
            'last_login', 'date_joined')}),
    ]
    add_form = UserCreationFormExtended
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1',
                       'password2',)
        }),
    )
    ordering = ('-date_joined',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
