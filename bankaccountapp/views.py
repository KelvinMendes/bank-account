from django.shortcuts import render
from rest_framework import serializers, viewsets, views, status
from bankaccountapp.models import Client, Transaction
from bankaccountapp.serializer import ClientSerializer, TransactionSerializer
from rest_framework.response import Response

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TransactionViewSet(views.APIView):
    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The transaction has been done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)