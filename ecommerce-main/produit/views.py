from django.shortcuts import render
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from django.core import serializers
from .serializers import ProduitSerializer
from django.http import JsonResponse
from django.db.models import Q
from commande.models import Commande, Constituer
from .models import Produit
from categorie.models import Categorie
from client.models import Client
from livraison.models import Livraison
from recu.models import Recu
import json
import datetime
from .utily import cartCookie, cartData

# Create your views here.
def home(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.all()
    cuissons = Produit.objects.filter(categorie__nom="Cuisson")
    froids = Produit.objects.filter(categorie__nom="Froid")
    lavages = Produit.objects.filter(categorie__nom="Lavage")
    preparations = Produit.objects.filter(categorie__nom="Préparation culinaire")
    repassages = Produit.objects.filter(categorie__nom="Repassage")
    entretiens = Produit.objects.filter(categorie__nom="Entretien")
    
    data = cartData(request)
    cartItems = data['cartItems']
    commande = data['commande']
    items = data['items']
 
    context = {"produits": produits, 
               "cuissons": cuissons, 
               "froids": froids, 
               "lavages": lavages,
               "preparations": preparations,
               "repassages": repassages,
               "entretiens": entretiens,
               "cartItems": cartItems,
               "items": items,
               "commande": commande,
               "categories":categories,
               }

    return render(request, 'produit/home.html', context)


############################################################################

def edit(request, id):
    categories = Categorie.objects.all()
    produit = Produit.objects.get(id=id)
    categorie = produit.categorie
    produits = Produit.objects.filter(categorie__nom=categorie)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'produit': produit, 'produits': produits, "cartItems": cartItems, "categories":categories, }
    return render(request, 'produit/product.html', context)

def test(request):
    data = cartData(request)
    cartItems = data['cartItems']
    produits = Produit.objects.all()
    if request.user.is_authenticated:
        client = request.user.utilisateur.client
        commande = Commande.objects.latest('id')
    context = {"commande": commande}
#JsonResponse({"cartItems": cartItems, "commande": commande})
    return render(request, 'admin/index.html', context)
##########################################################################

def panier(request):
    categories = Categorie.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    commande = data['commande']
    items = data['items']
            
    context = {"items": items, "commande": commande, "cartItems": cartItems, "categories":categories,}
    return render(request, 'produit/panier.html', context)

###################################################################################################

def checkout(request):
    categories = Categorie.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    commande = data['commande']
    items = data['items']
    client = data['client']        
   
    context = {"items": items, "commande": commande, "cartItems": cartItems, "categories":categories,}
    
    return render(request, 'produit/checkout.html', context)

##################################################################################################
def updateItems(request):
   
    data = json.loads(request.body)
    #data = request.GET['data']
    #productId = request.GET['productId']
    #action = request.GET['action']
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('ProductId:', productId)

    client = request.user.utilisateur.client
    produit = Produit.objects.get(id=productId)
    commande, created = Commande.objects.get_or_create(client=client, etat_commande='en instance')
    item, created = Constituer.objects.get_or_create(commande=commande, produit=produit)

    if action == 'add':
        item.qte_produit += 1
    elif action == 'remove':
        item.qte_produit -= 1
    item.save()
    
    if action == 'delete':
        item.delete()
    if item.qte_produit <= 0:
        item.delete()

    return JsonResponse('data was added', safe=False)

#######################################################################################################

def processOrder(request):
    print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    dataForm = json.loads(request.body)

    if request.user.is_authenticated:
        client = request.user.utilisateur.client
        commande, created = Commande.objects.get_or_create(client=client, etat_commande='en instance')

    nom = dataForm['form']['nom']
    #prenom = dataForm['form']['prenom']
    email = dataForm['form']['email']
    adresse = dataForm['form']['adresse']
    numero = dataForm['form']['numero']
    rue = dataForm['livraison']['lieu_livraison']
    cart = dataForm['cart']

    client.numero = numero
    client.email = email
    client.quartier = adresse
    client.rue = rue
    client.no_de_maison = nom
    client.save()

    prix = float(dataForm['livraison']['prix_total'])
    #commande = Commande.objects.create(client=client, etat_commande='non livré', transaction_id=transaction_id)
    commande.etat_commande = 'non livré'
    commande.transaction_id = transaction_id
    commande.save()
    for i in cart:
        qte_produit = cart[i]['qte_produit']
        produit = Produit.objects.get(id=i)
        Constituer.objects.create(
            qte_produit = qte_produit,
            produit = produit,
            commande = commande
        )
    recu = Recu.objects.create(commande=commande)

    Livraison.objects.create(
        client = client,
        commande = commande
        )
       
   
    #message = "cet email existe déjà"
    #context = {"message": message}  
    #render(request, 'produit/checkout.html', context)
    #JsonResponse('form data send correctly ...', safe=False)
    return JsonResponse('form data send correctly ...', safe=False)

def contact(request):
    categories = Categorie.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    
    context = {'cartItems':cartItems, "categories":categories,}
    return render(request, 'base/contact.html', context)

def apropos(request):
    categories = Categorie.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems':cartItems, "categories":categories,}
    return render(request, 'base/apropos.html', context)

def product_by_categorie(request):
    data = json.loads(request.body)
    cat_id = data['categorie_id']
    #produits = Produit.objects.filter(categorie=cat_id)
    produits = serializers.serialize("json",Produit.objects.filter(categorie=cat_id))
    #json_id = serializers.serializer([produit.id for produit in produits])
    #data = cartData(request)
    #cartItems = data['cartItems']
    response = {'json_data': produits}
    
    return JsonResponse(response)

def produits(request):
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    
    cuissons = Produit.objects.filter(categorie__nom="Cuisson")
    froids = Produit.objects.filter(categorie__nom="Froid")
    lavages = Produit.objects.filter(categorie__nom="Lavage")
    preparations = Produit.objects.filter(categorie__nom="Préparation culinaire")
    repassages = Produit.objects.filter(categorie__nom="Repassage")
    entretiens = Produit.objects.filter(categorie__nom="Entretien")
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems':cartItems,
        'cuissons': cuissons,
        'froids':froids,
        'lavages':lavages,
        'preparations':preparations,
        'entretiens':entretiens,
        'repassages':repassages,
        'produits':produits,
        'categories':categories,

    }
    return render(request, 'produit/produits.html', context)

def categorie(request, pk):
    categorie = Categorie.objects.get(id=pk)
    categories = Categorie.objects.all()
    produits = Produit.objects.filter(categorie=categorie)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {"produits": produits, "cartItems":cartItems, 'categories':categories, 'categorie':categorie}
    return render(request, 'produit/produits.html', context)

def search(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    categories = Categorie.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        multiple_q = Q(Q(nom__icontains=q)|Q(categorie__nom__icontains=q))
        produits = Produit.objects.filter(multiple_q)
    else:
      produits = []
    context = {"produits": produits, "categories":categories, "cartItems":cartItems, }
    
    return render(request, 'produit/search.html', context)

def paiement(request):
    data = cartData(request)
    cartItems = data['cartItems']
    auth_token = "7e3a2f6d-e6b9-40ac-96bb-25f8488188df"
    context = {"cartItems":cartItems,"auth_token":auth_token}
    return render(request, 'produit/paiement.html', context)

def recu(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {"cartItems":cartItems, }
    return render(request, 'produit/recu.html', context)

def commande(request):
    data = cartData(request)
    cartItems = data['cartItems']
    client = request.user.utilisateur.client
    id = Commande.objects.latest('id').id
    commandes = Commande.objects.filter(client=client).exclude(transaction_id=None)
    context = {"cartItems":cartItems,"commandes": commandes}
    return render(request, 'produit/commande.html', context)



#Création d'utlisateur non connecté
"""else:
            print('User is not autenticate!')
            print('COOKIES:', request.COOKIES)
            nom = dataForm['form']['nom']
            prenom = dataForm['form']['prenom']
            email = dataForm['form']['email']
            adresse = dataForm['form']['adresse']
            numero = dataForm['form']['numero']
        

            cookieData = cartCookie(request)
            items = cookieData['items']
            
        
            
            client, created = Client.objects.get_or_create(email=email)
            client.nom = nom
            client.prenom = prenom
            client.adresse = adresse
            client.numero = numero
            client.save()
           

            
            commande = Commande.objects.create(client=client, etat_commande='en instance')
   
            
        
            for item in items:
                produit = Produit.objects.get(id=item['produit']['id'])
                constituer = Constituer.objects.create(produit=produit, commande=commande, qte_produit=item['qte_produit'])
        """


 #API rest --------------------------------------------------------------------------------------->>
# @api_view(['GET'])
# def allProduit(request):
#     produits = Produit.objects.all()
#     serialization = ProduitSerializer(produits, many=True)
#     return Response(serialization.data)

"""@api_view(['GET'])
def getProduit(request, id):
    produit = Produit.objects.get(id=id)
    serialization = ProduitSerializer(produit)
    return Response(serialization.data)

@api_view(['POST'])
def addProduit(request):
    serializer = ProduitSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateProduit(request, id):
    produit = Produit.objects.get(id=id)
    serialization = ProduitSerializer(instance=produit, data=request.data)
    if serialization.is_valid():
        serialization.save()
    return Response(serialization.data)

@api_view(['DELETE'])
def deleteProduit(request, id):
    produit = Produit.objects.get(id=id)
    produit.delete()
    return Response("Produit supprimé avec succès!")

"""
