from django.shortcuts import render
from rest_framework import serializers, viewsets, generics
from bankaccountapp.models import Client, Account
from bankaccountapp.serializer import ClientSerializer, AccountSerializer 


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer    