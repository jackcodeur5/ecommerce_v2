from django.db import models
from commande.models import Commande
from client.models import Client

# Create your models here.
class Livraison(models.Model):
    #prix_livraison = models.FloatField(null =True)
    #nom_destinataire = models.CharField(max_length=200, null=True)
    #prenom_destinataire = models.CharField(max_length=200, null=True)
    #email = models.EmailField(null=True)
    #numero = models.IntegerField(null=True)
    #destination = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now = True)

    def __str__(self):
        return "Livraison#" + f"{self.id} "
