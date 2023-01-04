# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import LivraisonSerializer
# from .models import Livraison

# # Create your views here.



# #API REST 
# @api_view(['GET'])
# def allLivraisons(request):
#     livraisons = Livraison.objects.all()
#     serialization = LivraisonSerializer(livraisons, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getLivraison(request, id):
#     livraison = Livraison.objects.get(id=id)
#     serialization = LivraisonSerializer(livraison)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addLivraison(request):
#     serializer = LivraisonSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateLivraison(request, id):
#     livraison = Livraison.objects.get(id=id)
#     serialization = LivraisonSerializer(instance=livraison, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteLivraison(request, id):
#     livraison = Livraison.objects.get(id=id)
#     livraison.delete()
#     return Response("Livraison supprimé avec succès!")
