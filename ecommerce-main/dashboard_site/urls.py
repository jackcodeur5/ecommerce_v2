from django.urls import path
from .views import *

urlpatterns = [
    path("index", index, name="dashboard_index"),
    path("profile", profile, name="dashboard_profile"),
    path("produit", produit, name="dashboard_produit"),
    path("create", create_produit, name="dashboard_create_produit"),
    path("update/<str:pk>", update_produit, name="dashboard_update_produit"),
    path("delete/<str:pk>", delete_produit, name="dashboard_delete_produit"),

    path("categorie", categorie, name="dashboard_categorie"),
    path("categorie/create", create_categorie, name="dashboard_create_categorie"),
    path("categorie/update/<str:pk>", update_categorie, name="dashboard_update_categorie"),
    path("categorie/delete/<str:pk>", delete_categorie, name="dashboard_delete_categorie"),

    path("client", client, name="dashboard_client"),
    path("client/delete/<str:pk>", delete_client, name="dashboard_delete_client"),

    path("vendeur", vendeur, name="dashboard_vendeur"),
    path("vendeur/delete/<str:pk>", delete_vendeur, name="dashboard_delete_vendeur"),

    path("commande", commande, name="dashboard_commande"),
    path("commande/<str:pk>", edit_commande, name="dashboard_edit_commande"),
    path("commande/delete/<str:id>", delete_commande, name="dashboard_delete_commande"),
    path("commande/update/<str:pk>", update_commande, name="dashboard_update_commande"),

    path("user", user, name="dashboard_user"),
    path("user/create", create_user, name="dashboard_create_user"),
    path("user/update/<str:pk>", update_user, name="dashboard_update_user"),
    path("user/delete/<str:pk>", delete_user, name="dashboard_delete_user"),

    

]