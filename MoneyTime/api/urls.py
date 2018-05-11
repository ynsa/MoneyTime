
# django
from django.conf.urls import url
from django.conf.urls import include

# 3rd party
from rest_framework import routers
# from rest_framework.documentation import include_docs_urls

from MoneyTime.api import views as api_views

router = routers.DefaultRouter()
router.register(r'user', api_views.UserViewSet, 'user')
router.register(r'expense', api_views.ExpenseViewSet, 'expense')
router.register(r'expense_category', api_views.ExpenseCategoryViewSet, 'expense_category')
router.register(r'location', api_views.LocationViewSet, 'location')
router.register(r'location_category', api_views.LocationCategoryViewSet, 'location_category')

# urls for Django Rest Framework API
urlpatterns = [
    url(r'v1/', include(router.urls)),

    # url(r'v1/obtain_token/', api_views.ObtainExpiringAuthToken.as_view()),

    # url(r'docs/', include_docs_urls(
    #     title='MoneyTime API',
    #     authentication_classes=[],
    #     permission_classes=[]
    # )),
]
