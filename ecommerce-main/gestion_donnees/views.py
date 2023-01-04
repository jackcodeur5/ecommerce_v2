from django.shortcuts import render, redirect
from django.contrib import messages
from produit.models import Produit
from produit.utily import *
from client.models import Client
from livraison.models import Livraison
from .forms import *

# Create your views here.
#Gestion des données des produits

def index(request):
    produits = Produit.objects.all()
    context = {"produits": produits}
    return render(request, 'admin/produits/index.html', context)

def index_site(request):
    client = request.user.utilisateur.client
    commandes = Commande.objects.filter(client=client).exclude(transaction_id=None)
    nombre = commandes.count
    data = cartData(request)
    cartItems = data['cartItems']
    context = {"commandes": commandes, "nombre": nombre, "cartItems": cartItems}
    return render(request, 'admin/index.html', context)


def create(request):
    form = formProduit()
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " produit créé avec succes!")
            return redirect('produit_index')
    context = {"form": form}
    return render(request, 'admin/produits/create.html', context)

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

#Gestion des données des clients

def indexClient(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, 'admin/clients/index.html', context)

def createClient(request):
    form = CreerClient()
    if request.method == 'POST':
        form = CreerClient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "client créé avec succès!")
            return redirect('client_index')
    context = {"form": form}
    return render(request, 'admin/clients/create.html', context)

def editClient(request, pk):
    client = Client.objects.get(id=pk)
    context = {"client":client}
    return render(request, 'admin/clients/edit.html', context)

def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = CreerClient(instance=client) 
    if request.method == 'POST':
        form = CreerClient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client modifié avec succès !")
            return redirect('client_index')
    context = {'form': form}
    return render(request, 'admin/clients/update.html', context)
"""
def updateClient(request, pk):
    client=Client.objects.get(id=pk)
    form = CreerClient(instance=client)
    if request.method == 'POST':
        form = CreerClient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "client modifié avec succès!")
            return redirect('client_index')
    context = {'form': form}
    return render(request, 'admin/clients/update.html', context)
"""
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    messages.success(request, "client supprimé avec succès!")
    return redirect('client_index')

#Gestion des données des commades

def indexCommande(request):
    client = request.user.utilisateur.client
    id = Commande.objects.latest('id').id
    commandes = Commande.objects.filter(client=client).exclude(transaction_id=None)
    context = {"commandes": commandes}
    return render(request, 'admin/commandes/index.html', context)

def createCommande(request):
    form = formCommande()
    if request.method == 'POST':
        form = formCommande(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "commande créer avec succès!")
            return redirect('commande_index')
    context = {"form": form}
    return render(request, 'admin/commandes/create.html', context)

def editCommande(request, pk):
    commande = Commande.objects.get(id=pk)
    items = commande.constituer_set.all()
    livraisons = Livraison.objects.filter(commande=commande)
    context = {"items":items, "commande":commande, "livraisons":livraisons}
    return render(request, 'admin/commandes/edit.html', context)

def updateCommande(request, pk):
    commande=Commande.objects.get(id=pk)
    items = commande.constituer_set.all()
    form = formCommande(instance=commande)
    if request.method == 'POST':
        form = formCommande(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "commande modifiée avec succès!")
            return redirect('commande_index')
    context = {'form': form, "commande":commande, "items":items}
    return render(request, 'admin/commandes/update.html', context)

def deleteCommande(request, pk):
    commande = Commande.objects.get(id=pk)
    commande.delete()
    messages.success(request, "commande supprimée avec succès!")
    return redirect('commande_index')

#Gestion des données des livraisons

def indexLivraison(request):
    livraisons = Livraison.objects.all()
    context = {"livraisons": livraisons}
    return render(request, 'admin/livraisons/index.html', context)

def createLivraison(request):
    form = formLivraison()
    if request.method == 'POST':
        form = formLivraison(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "livraison créer avec succès!")
            return redirect('livraison_index')
    context = {"form": form}
    return render(request, 'admin/livraisons/create.html', context)

def editLivraison(request, pk):
    livraison = Livraison.objects.get(id=pk)
    context = {"livraison":livraison}
    return render(request, 'admin/livraisons/edit.html', context)

def updateLivraison(request, pk):
    livraison=Livraison.objects.get(id=pk)
    form = formLivraison(instance=livraison)
    if request.method == 'POST':
        form = formLivraison(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "livraison modifiée avec succès!")
            return redirect('livraison_index')
    context = {'form': form, "livraison":livraison }
    return render(request, 'admin/livraisons/update.html', context)

def deleteLivraison(request, pk):
    livraison = Livraison.objects.get(id=pk)
    livraison.delete()
    messages.success(request, "livraison supprimée avec succès!")
    return redirect('livraison_index')

#test
def testlist(request):
    return render(request, 'base/test.html')