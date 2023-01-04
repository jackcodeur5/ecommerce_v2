"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('superadmin/', admin.site.urls),
    #path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('produit.urls')),
    path('categorie/', include('categorie.urls')),
    path('client/', include('client.urls')),
    path('commande/', include('commande.urls')),
    path('livraison/', include('livraison.urls')),
    path('recu/', include('recu.urls')),
    path('utilisateur/', include('utilisateur.urls')),
    path('vendeur/', include('vendeur.urls')),
    path('dashboard/', include('dashboard.urls')),
    # path('account/', include('accounts.urls')),
    path('users-dashboard/', include('gestion_donnees.urls')),
    path('dashboard-site/', include('dashboard_site.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
