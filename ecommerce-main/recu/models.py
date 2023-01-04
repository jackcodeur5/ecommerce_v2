from django.db import models
from commande.models import Commande

# Create your models here.
class Recu(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "Recu de la  " + f"{self.commande} "