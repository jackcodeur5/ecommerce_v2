import json
from .models import Produit
from commande.models import Commande


def cartCookie(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    commande = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = commande['get_cart_items']
    for i in cart:
        try:   
            cartItems += cart[i]['qte_produit']
            produit = Produit.objects.get(id=i)
            total = (produit.prix_achat * cart[i]['qte_produit'])
            commande['get_cart_total'] += total
            commande['get_cart_items'] += cart[i]['qte_produit']
            item = {
                'produit': {
                    'id': produit.id,
                    'nom': produit.nom,
                    'prix_achat': produit.prix_achat,
                    'image': produit.image
                },
                'qte_produit': cart[i]['qte_produit'],
                'get_total': total
                }
            items.append(item)
        except:
            pass
    return {'cartItems':cartItems, 'commande': commande, 'items': items }

def cartData(request):
    if request.user.is_authenticated and cartCookie(request) != None:
        client = request.user.utilisateur.client
        commande, created = Commande.objects.get_or_create(client=client, etat_commande='en instance')
        items = commande.constituer_set.all()
        cartItems = commande.get_cart_items
        if cartItems == None:
            #commande = {}
            #cartItems = 0
            cookieData = cartCookie(request)
            cartItems = cookieData['cartItems']
            commande = cookieData['commande']
            items = cookieData['items']
        
    else:
        cookieData = cartCookie(request)
        cartItems = cookieData['cartItems']
        commande = cookieData['commande']
        items = cookieData['items']
        client = []
    return {'cartItems':cartItems, 'commande': commande, 'items': items, 'client': client }

def createRessource(request, Form):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
    return context

