from django.contrib import admin
from django.db import router
from django.urls import path, include
from bankaccountapp.views import ClientsViewSet, TransactionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clients', ClientsViewSet, basename='Clients')
#router.register('transactions', TransactionViewSet, basename='Transactions')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('transactions', TransactionViewSet.as_view()),
]
