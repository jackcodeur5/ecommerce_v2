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
    return render(request, 'dashboard-admin/index.html')

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
    return render(request, 'dashboard-admin/produit.html', context)

@login_required
def create_produit(request):
    form = formProduit()
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " produit créé avec succes!")
            return redirect('dashboard_produit')
    context = {"form": form}
    return render(request, 'dashboard-admin/create_produit.html', context)

@login_required
def update_produit(request, pk):
    produit=Produit.objects.get(id=pk)
    form = formProduit(instance=produit)
    if request.method == 'POST':
        form = formProduit(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "produit modifié avec succès!")
            return redirect('dashboard_produit')
    context = {'form': form, "produit": produit}
    return render(request, 'dashboard-admin/update_produit.html', context )

@login_required
def delete_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    produit.delete()
    messages.success(request, "produit supprimé avec succès!")
    return redirect('dashboard_produit')
###################################################
@login_required
def categorie(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'dashboard-admin/categorie.html', context)

@login_required
def create_categorie(request):
    form = formCategorie()
    if request.method == 'POST':
        form = formCategorie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " categorie créé avec succes!")
            return redirect('dashboard_categorie')
    context = {"form": form}
    return render(request, 'dashboard-admin/create_categorie.html', context)

@login_required
def update_categorie(request, pk):
    categorie=Categorie.objects.get(id=pk)
    form = formCategorie(instance=categorie)
    if request.method == 'POST':
        form = formCategorie(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, "categorie modifié avec succès!")
            return redirect('dashboard_categorie')
    context = {'form': form, "categorie": categorie}
    return render(request, 'dashboard-admin/update_categorie.html', context )

@login_required
def delete_categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    categorie.delete()
    return redirect('dashboard_categorie')
############################################################

@login_required
def client(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, 'dashboard-admin/client.html', context)

@login_required
def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    messages.success(request, "client supprimé avec succès!")
    return redirect('dashboard_client')


@login_required
def vendeur(request):
    vendeurs = Vendeur.objects.all()
    context = {"vendeurs": vendeurs}
    return render(request, 'dashboard-admin/vendeur.html', context)

@login_required
def delete_vendeur(request, pk):
    vendeur = Vendeur.objects.get(id=pk)
    vendeur.delete()
    messages.success(request, "Vendeur  supprimé avec succès!")
    return redirect('dashboard_vendeur')

@login_required
def commande(request):
    commandes = Commande.objects.exclude(transaction_id=None)
    context = {"commandes": commandes}
    return render(request, 'dashboard-admin/commande.html', context)

@login_required
def edit_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    items = commande.constituer_set.all()
    livraisons = Livraison.objects.filter(commande=commande)
    context = {"items":items, "commande":commande, "livraisons":livraisons}
    return render(request, 'dashboard-admin/edit_commande.html', context)

@login_required
def delete_commande(request, id):
    commande = Commande.objects.get(id=id)
    commande.delete()
    messages.success(request, "commande supprimée avec succès!")
    return redirect('dashboard_commande')


@login_required
def update_commande(request, pk):
    commande=Commande.objects.get(id=pk)
    if request.method == 'POST':
        etat = request.POST['etat']
        if etat == 'livré':
            commande.etat_commande = etat
            commande.save()
            messages.success(request, "commande modifiée avec succès!")
            return redirect('dashboard_commande')
        else:
             return HttpResponse("Attention la commande a été déjà livré ")
   
@login_required
def profile(request):
    return render(request, 'dashboard-admin/profile.html')


##################################################################

@login_required
def user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'dashboard-admin/user.html', context)

@login_required
def create_user(request):
    form = formUser()
    if request.method == 'POST':
        form = formUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " user créé avec succes!")
            return redirect('dashboard_user')
    context = {"form": form}
    return render(request, 'dashboard-admin/create_user.html', context)

@login_required
def update_user(request, pk):
    user=User.objects.get(id=pk)
    form = formUser(instance=user)
    if request.method == 'POST':
        form = formUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "user modifié avec succès!")
            return redirect('dashboard_user')
    context = {'form': form, "user": user}
    return render(request, 'dashboard-admin/update_user.html', context )

@login_required
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('dashboard_user')
