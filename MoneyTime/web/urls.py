from django.conf.urls import url

from MoneyTime.web import views

urlpatterns = [
    url(r'^$', views.ReactPage.as_view(), name='react'),
    url(r'^(?:.*)/?$', views.ReactPage.as_view(), name='react')
]
