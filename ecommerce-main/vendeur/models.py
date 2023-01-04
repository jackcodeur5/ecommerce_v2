from django.db import models
from utilisateur.models import Utilisateur

# Create your models here.
class Vendeur(Utilisateur):
    pass
    #nom = models.CharField(max_length=200, null=True)
    #prenom = models.CharField(max_length=200, null=True)
    #numero = models.CharField(max_length=200, null=True)
    #adresse = models.CharField(max_length=200, null=True)
    #compte = models.OneToOneField( Compte, on_delete=models.CASCADE, primary_key=True)
    #date_creation = models.DateTimeField(auto_now_add=True, null=True)
