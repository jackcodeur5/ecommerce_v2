from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from produit.models import Produit
from categorie.models import Categorie
from client.models import Client
from vendeur.models import Vendeur
from commande.models import Commande, Constituer
from livraison.models import Livraison
from django.contrib import messages
from gestion_donnees.forms import *
from django.db.models import Q


# Create your views here.
@login_required
def index(request):
	return render(request, 'dashboard/home.html')

@login_required
def categorie(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'dashboard/categorie.html', context)

@login_required
def create_categorie(request):
    form = formCategorie()
    if request.method == 'POST':
        form = formCategorie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Categorie créée avec succes!")
            return redirect('dashboard-categorie')
    context = {"form": form}
    return render(request, 'dashboard/create_categorie.html', context)

@login_required
def update_categorie(request, pk):
    categorie=Categorie.objects.get(id=pk)
    form = formCategorie(instance=categorie)
    if request.method == 'POST':
        form = formCategorie(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, "Categorie modifiée avec succès!")
            return redirect('dashboard-categorie')
    context = {'form': form, "categorie": categorie}
    return render(request, 'dashboard/update_categorie.html', context )

@login_required
def delete_categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    categorie.delete()
    return redirect('dashboard-categorie')

@login_required
def commande(request):
    commandes = Commande.objects.exclude(transaction_id=None)
    context = {"commandes": commandes}
    return render(request, 'dashboard/commande.html', context)

@login_required
def edit_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    items = commande.constituer_set.all()
    #livraisons = Livraison.objects.filter(commande=commande)
    context = {"items":items, "commande":commande}
    return render(request, 'dashboard/edit_commande.html', context)

@login_required
def delete_commande(request, id):
    commande = Commande.objects.get(id=id)
    commande.delete()
    messages.success(request, "Commande supprimée avec succès!")
    return redirect('dashboard-commande')


@login_required
def update_commande(request, pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        etat = request.POST['etat']
        if etat == 'livré':
            commande.etat_commande = etat
            commande.save()
            messages.success(request, "Commande modifiée avec succès!")
            return redirect('dashboard-commande')
        else:
             return HttpResponse("Attention la commande a été déjà livrée ")

@login_required
def produit(request):
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        multiple_q = Q(Q(nom__icontains=q)|Q(categorie__nom__icontains=q))
        produits = Produit.objects.filter(multiple_q)
    else:
        produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'dashboard/produit.html', context)

@login_required
def create_produit(request):
    form = formProduit()
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Produit créé avec succes!")
            return redirect('dashboard-produit')
    context = {"form": form}
    return render(request, 'dashboard/create_produit.html', context)

@login_required
def update_produit(request, pk):
    produit=Produit.objects.get(id=pk)
    form = formProduit(instance=produit)
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié avec succès!")
            return redirect('dashboard-produit')
    context = {'form': form, "produit": produit}
    return render(request, 'dashboard/update_produit.html', context )

@login_required
def delete_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    produit.delete()
    messages.success(request, "Produit supprimé avec succès!")
    return redirect('dashboard-produit')
###################################################

@login_required
def client(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, 'dashboard/client.html', context)

@login_required
def create_client(request):
    form = formClient()
    if request.method == 'POST':
        form = formClient(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Client créé avec succes!")
            return redirect('dashboard-client')
    context = {"form": form}
    return render(request, 'dashboard/create_client.html', context)

@login_required
def update_client(request, pk):
    client=Client.objects.get(id=pk)
    form = formClient(instance=client)
    if request.method == 'POST':
        form = formClient(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client modifié avec succès!")
            return redirect('dashboard-client')
    context = {'form': form, "client": client}
    return render(request, 'dashboard/update_client.html', context )

@login_required
def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    messages.success(request, "Client supprimé avec succès!")
    return redirect('dashboard-client')

@login_required
def vendeur(request):
    vendeurs = Vendeur.objects.all()
    context = {"vendeurs": vendeurs}
    return render(request, 'dashboard/vendeur.html', context)

@login_required
def create_vendeur(request):
    form = formVendeur()
    if request.method == 'POST':
        form = formVendeur(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Vendeur créé avec succes!")
            return redirect('dashboard-vendeur')
    context = {"form": form}
    return render(request, 'dashboard/create_vendeur.html', context)

@login_required
def update_vendeur(request, pk):
    vendeur=Vendeur.objects.get(id=pk)
    form = formVendeur(instance=vendeur)
    if request.method == 'POST':
        form = formVendeur(request.POST, request.FILES, instance=vendeur)
        if form.is_valid():
            form.save()
            messages.success(request, "Vendeur modifié avec succès!")
            return redirect('dashboard-vendeur')
    context = {'form': form, "vendeur": vendeur}
    return render(request, 'dashboard/update_vendeur.html', context )

@login_required
def delete_vendeur(request, pk):
    vendeur = Vendeur.objects.get(id=pk)
    vendeur.delete()
    messages.success(request, "Vendeur  supprimé avec succès!")
    return redirect('dashboard-vendeur')
