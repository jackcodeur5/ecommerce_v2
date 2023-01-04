from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Utilisateur
from client.models import Client
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
		fields = ['nom', 'prenom']