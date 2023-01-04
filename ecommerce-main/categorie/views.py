# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import CategorieSerializer
# from .models import Categorie

# # Create your views here.














# #api rest
# @api_view(['GET'])
# def allCategories(request):
#     categorie = Categorie.objects.all()
#     serialization = CategorieSerializer(categorie, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getCategorie(request, id):
#     categorie = Categorie.objects.get(id=id)
#     serialization = CategorieSerializer(categorie)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addCategorie(request):
#     serializer = CategorieSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateCategorie(request, id):
#     categorie = Categorie.objects.get(id=id)
#     serialization = CategorieSerializer(instance=categorie, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteCategorie(request, id):
#     categorie = Categorie.objects.get(id=id)
#     categorie.delete()
#     return Response("Categorie supprimée avec succès!")