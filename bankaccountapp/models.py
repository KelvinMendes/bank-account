from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()


class Transaction(models.Model):
    balance = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
