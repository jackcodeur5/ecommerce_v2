from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='vendeur_index'),
    path('home', views.home, name='home_vendeur'),
    path('create', views.create, name='create_produit'),
    path('vendeur', views.vendeur, name='vendeur'),

   
]

#  path('allvendeur/', views.allVendeurs),
#     path('getvendeur/<int:id>/', views.getVendeur),
#     path('addvendeur/', views.addVendeur),
#     path('updatevendeur/<int:id>/', views.updateVendeur),
#     path('deletevendeur/<int:id>/', views.deleteVendeur),