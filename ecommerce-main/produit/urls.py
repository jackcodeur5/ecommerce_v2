from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('page_produit/<int:id>/', views.edit, name='detail'),
    path('panier/', views.panier, name='panier'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_items/', views.updateItems, name='update_items'),
    path('process_order/', views.processOrder, name='process_order'),
    path('test', views.test, name='test'),
    path('paiement', views.paiement, name='paiement'),
    path('contact', views.contact, name='contact'),
    path('apropos', views.apropos, name='apropos'),
    path('produits', views.produits, name='produits'),
    path('categorie/<str:pk>/', views.categorie, name="categorie"),
    path('search', views.search, name="search"),
    path('recu', views.recu, name="recu_paiement"),
    path('commande', views.commande, name="commande"),
    path('product_by_categorie', views.product_by_categorie, name="product_by_categorie")
    ]

"""
    path('produits/', views.allProduit),
    path('produit/<int:id>/', views.getProduit),
    path('addproduit/', views.addProduit),
    path('updateproduit/<int:id>/', views.updateProduit),
    path('deleteproduit/<int:id>/', views.deleteProduit),
    path('produits/', views.allProduit),
"""

