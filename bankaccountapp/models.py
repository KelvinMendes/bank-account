from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()


class Account(models.Model):
    agency = models.IntegerField()
    account = models.IntegerField()
    balance = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
