# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import CommandeSerializer
# from .models import Commande

# # Create your views here.



# #API REST 
# @api_view(['GET'])
# def allCommandes(request):
#     commandes = Commande.objects.all()
#     serialization = CommandeSerializer(commandes, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getCommande(request, id):
#     commande = Commande.objects.get(id=id)
#     serialization = CommandeSerializer(commande)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addCommande(request):
#     serializer = CommandeSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateCommande(request, id):
#     commande = Commande.objects.get(id=id)
#     serialization = CommandeSerializer(instance=commande, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteCommande(request, id):
#     commande = Commande.objects.get(id=id)
#     commande.delete()
#     return Response("Commande supprimé avec succès!")
