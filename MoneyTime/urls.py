from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^favicon.ico$',
        RedirectView.as_view(url='/staticfiles/design/favicon.ico', permanent=True)
    ),
    url(r'^api/', include('MoneyTime.api.urls')),
    url(r'^', include('MoneyTime.web.urls')),
]

