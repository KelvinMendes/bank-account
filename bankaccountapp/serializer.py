from django.db import models
from django.db.models import fields
from rest_framework import serializers
from bankaccountapp.models import Client, Account
from rest_framework.response import Response


class ClientSerializer(serializers.ModelSerializer):
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
         
    class Meta:
        model = Client
        fields = '__all__' #['name', 'cpf']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__' 