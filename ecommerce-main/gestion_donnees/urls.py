from django.urls import path
from .views import *

urlpatterns = [
    path("index", index_site, name="users_dashboard_index"),
    path("commande_index", indexCommande, name="commande_index"),
    path("commande_create", createCommande, name="commande_create"),
    path("commande_edit/<str:pk>", editCommande, name="commande_edit"),
    path("commande_update/update/<str:pk>", updateCommande, name="commande_update"),
    path("commande_delete/<str:pk>", deleteCommande, name="commande_delete"),  
]


"""path("livraison_index", indexLivraison, name="livraison_index"),
    path("livraison_create", createLivraison, name="livraison_create"),
    path("livraison_edit/<str:pk>", editLivraison, name="livraison_edit"),
    path("livraison_update/<str:pk>", updateLivraison, name="livraison_update"),
    path("livraison_delete/<str:pk>", deleteLivraison, name="livraison_delete"),
    path("test", testlist, name="test_admin"),

 path("client_index", indexClient, name="client_index"),
    path("client_create", createClient, name="client_create"),
    path("client_edit/<str:pk>", editClient, name="client_edit"),
    path("client_update/<str:pk>", updateClient, name="client_update"),
    path("client_delete/<str:pk>", deleteClient, name="client_delete"),

path("produit_index", index, name="produit_index"),
    path("produit_create", create, name="produit_create"),
    path("produit_edit/<str:pk>", edit, name="produit_edit"),
    path("produit_update/<str:pk>", update, name="produit_update"),
    path("produit_delete/<str:pk>", delete, name="produit_delete"),"""