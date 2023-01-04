from django.db import models
from utilisateur.models import Utilisateur

# Create your models here.
class Client(Utilisateur):
    pass 
    #nom = models.CharField(max_length=200, null=True)
    #prenom = models.CharField(max_length=200, null=True)
    #numero = models.IntegerField()
    #email = models.EmailField()
    #adresse = models.CharField(max_length=200, null=True)
    #date_creation = models.DateTimeField(auto_now_add=True, null=True)