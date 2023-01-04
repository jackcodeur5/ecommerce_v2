from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    numero = models.IntegerField(null=True)
    #adresse = models.CharField(max_length=200, null=True)
    quartier = models.CharField(max_length=200, null=True)
    rue = models.CharField(max_length=200, null=True)
    no_de_maison = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now=True, null=True)
    #pass_word = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom