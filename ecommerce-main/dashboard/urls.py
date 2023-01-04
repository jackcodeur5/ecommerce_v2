from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
	path('categorie', views.categorie, name='dashboard-categorie'),
	path('categorie/create', views.create_categorie, name='dashboard-categorie-create'),
	path("categorie/update/<str:pk>", views.update_categorie, name="dashboard-categorie-update"),
	path("categorie/delete/<str:pk>", views.delete_categorie, name="dashboard-categorie-delete"),

	path("commande", views.commande, name="dashboard-commande"),
    path("commande/<str:pk>", views.edit_commande, name="dashboard-commande-edit"),
    path("commande/delete/<str:id>", views.delete_commande, name="dashboard-commande-delete"),
    path("commande/update/<str:pk>", views.update_commande, name="dashboard-commande-update"),

	path("produit", views.produit, name="dashboard-produit"),
    path("produit/create", views.create_produit, name="dashboard-produit-create"),
    path("produit/update/<str:pk>", views.update_produit, name="dashboard-produit-update"),
    path("produit/delete/<str:pk>", views.delete_produit, name="dashboard-produit-delete"),

	
    path("client", views.client, name="dashboard-client"),
	path("client/create", views.create_client, name="dashboard-client-create"),
	path("client/update/<str:pk>", views.update_client, name="dashboard-client-update"),
    path("client/delete/<str:pk>", views.delete_client, name="dashboard-client-delete"),

	path("vendeur", views.vendeur, name="dashboard-vendeur"),
	path("vendeur/create", views.create_vendeur, name="dashboard-vendeur-create"),
	path("vendeur/update/<str:pk>", views.update_vendeur, name="dashboard-vendeur-update"),
    path("vendeur/delete/<str:pk>", views.delete_vendeur, name="dashboard-vendeur-delete"),
   
    ]



