from django.db import models
from django.db.models import fields
from django.db.models import Sum
from rest_framework import serializers
from bankaccountapp.models import Client, Transaction
from rest_framework.response import Response


class ClientSerializer(serializers.ModelSerializer):
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 dígitos')
         
    class Meta:
        model = Client
        fields = '__all__' #['name', 'cpf']


class TransactionSerializer(serializers.ModelSerializer):
    def validate_balance(self, obj):
        client_id = self.initial_data['client']
        balance_value = obj
        balance = Transaction.objects.filter(client=client_id).aggregate(Sum('balance'))
        if (balance+balance_value) < 0:
            raise serializers.ValidationError('Insufficient balance')

    class Meta:
        model = Transaction
        fields = '__all__'
