from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import ClientSerializer
from .models import Client

# Create your views here.



# #API REST 
# @api_view(['GET'])
# def allClients(request):
#     clients = Client.objects.all()
#     serialization = ClientSerializer(clients, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getClient(request, id):
#     client = Client.objects.get(id=id)
#     serialization = ClientSerializer(client)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addClient(request):
#     serializer = ClientSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateClient(request, id):
#     client = Client.objects.get(id=id)
#     serialization = ClientSerializer(instance=client, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteClient(request, id):
#     client = Client.objects.get(id=id)
#     client.delete()
#     return Response("Client supprimé avec succès!")
