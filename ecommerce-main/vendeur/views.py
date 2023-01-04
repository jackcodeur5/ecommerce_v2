from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from .serializers import VendeurSerializer
from django.http import JsonResponse
from django.contrib import messages
from produit.models import Produit
from utilisateur.models import Utilisateur
from produit.utily import *
from client.models import Client
from gestion_donnees.forms import *
from .models import Vendeur

# Create your views here.
def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {"cartItems":cartItems}
    return render(request, 'vendeur/index.html', context)

def home(request):
    return render(request, 'vendeur/home.html')

def create(request):
    form = formProduitVendeur()
    if request.method == 'POST':
        form = formProduitVendeur(request.POST, request.FILES)
        print(vendeur)
        if form.is_valid():
            form.save()
            vendeur = request.user.utilisateur.client
            nom = form['nom'].value()
            categorie = form['categorie'].value()
            prix = form['prix_achat'].value()
            marque = form['marque'].value()
            print(nom)
            print(prix)
            produit = Produit.objects.filter(nom=nom, prix_achat=prix, marque=marque)
            produit.vendeurs = vendeur
            print(produit.vendeurs)
            produit.save()
            print(form['vendeurs'].value())
            messages.success(request, " produit créé avec succes!")
            return redirect('home_vendeur')
    context = {"form": form}
    return render(request, 'vendeur/create.html', context)

def edit(request, pk):
    produit = Produit.objects.get(id=pk)
    context = {"produit":produit}
    return render(request, 'admin/produits/edit.html', context)

def update(request, pk):
    produit=Produit.objects.get(id=pk)
    form = formProduit(instance=produit)
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "produit modifié avec succès!")
            return redirect('produit_index')
    context = {'form': form}
    return render(request, 'admin/produits/update.html', context )

def delete(request, pk):
    produit = Produit.objects.get(id=pk)
    produit.delete()
    messages.success(request, "produit supprimé avec succès!")
    return redirect('produit_index')

def vendeur(request):
    data = json.loads(request.body)
    vendeur = data['vendeur']
    client = request.user.utilisateur.client
    id = client.id
    user_id = Client.objects.get(id=id)
    Vendeur.objects.create(user=request.user)

    return JsonResponse('data was added', safe=False)



# #API REST 
# @api_view(['GET'])
# def allVendeurs(request):
#     vendeurs = Vendeur.objects.all()
#     serialization = VendeurSerializer(vendeurs, many=True)
#     return Response(serialization.data)

# @api_view(['GET'])
# def getVendeur(request, id):
#     vendeur = Vendeur.objects.get(id=id)
#     serialization = VendeurSerializer(vendeur)
#     return Response(serialization.data)

# @api_view(['POST'])
# def addVendeur(request):
#     serializer = VendeurSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateVendeur(request, id):
#     vendeur = Vendeur.objects.get(id=id)
#     serialization = VendeurSerializer(instance=vendeur, data=request.data)
#     if serialization.is_valid():
#         serialization.save()
#     return Response(serialization.data)

# @api_view(['DELETE'])
# def deleteVendeur(request, id):
#     vendeur = Vendeur.objects.get(id=id)
#     vendeur.delete()
#     return Response("Vendeur supprimé avec succès!")
