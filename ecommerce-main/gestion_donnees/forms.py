from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from utilisateur.models import Utilisateur
from client.models import Client
from produit.models import Produit
from categorie.models import Categorie
from commande.models import Commande
from livraison.models import Livraison
from vendeur.models import Vendeur
from django import forms

class CreerUtilisateur(UserCreationForm):
	"""docstring for CommandeForm"""
	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ['username',  'password1', 'password2']
		
class CreateUtilisateur(forms.ModelForm):
	class Meta:
		model = Utilisateur	
		fields = '__all__'		

class CreerClient(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['nom', 'prenom', 'email', 'numero', 'quartier', 'rue', 'no_de_maison']

class formProduit(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class formProduitVendeur(forms.ModelForm):
    class Meta:
        model = Produit
        exclude = ['vendeurs']

class formCommande(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['etat_commande']

class formLivraison(forms.ModelForm):
    class Meta:
        model = Livraison
        fields = '__all__'

class formCategorie(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class formUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class formClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class formVendeur(forms.ModelForm):
    class Meta:
        model = Vendeur
        fields = '__all__'