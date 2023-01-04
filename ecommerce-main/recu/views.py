from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .serializers import RecuSerializer
from .models import Recu

# Create your views here.



#API REST 
# @api_view(['GET'])
# def allRecus(request):
#     recus = Recu.objects.all()
#     serialization = RecuSerializer(recus, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getRecu(request, id):
#     recu = Recu.objects.get(id=id)
#     serialization = RecuSerializer(recu)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addRecu(request):
#     serializer = RecuSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateRecu(request, id):
#     recu = Recu.objects.get(id=id)
#     serialization = RecuSerializer(instance=recu, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteRecu(request, id):
#     recu = Recu.objects.get(id=id)
#     recu.delete()
#     return Response("Recu supprimé avec succès!")
