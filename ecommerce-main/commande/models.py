from django.db import models
from client.models import Client 
#from livraison.models import Livraison 
from produit.models import Produit

# Create your models here.
class Commande(models.Model):
    STATUS = (('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré'))
    transaction_id = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #total_commande = models.IntegerField(null=True)
    #mode_paiement = models.CharField(max_length=200, null=True)
    etat_commande = models.CharField(max_length=200, null=True, choices=STATUS)
    #date_commande = models.DateTimeField(null=True)
    #date_reglement = models.DateTimeField(null=True)
    produits = models.ManyToManyField(Produit, through='Constituer')
    date_creation = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "commande#" + f"{self.id}" 

    @property
    def get_cart_total(self):
        constituers = self.constituer_set.all()
        for constituer in constituers:
            if constituer.commande.etat_commande == 'en instance' or constituer.commande.etat_commande == 'non livré' or constituer.commande.etat_commande == 'livré':
                total = sum([item.get_total for item in constituers])
            else:
                total = 0
            return total
    
    @property
    def get_cart_items(self):
        constituers = self.constituer_set.all()
        for constituer in constituers:
            if constituer.commande.etat_commande == 'en instance' or constituer.commande.etat_commande == 'non livré' or constituer.commande.etat_commande == 'livré':
                total = sum([item.qte_produit for item in constituers])
            else:
                total = 0
            return total
    

class Constituer(models.Model):
    #nom_produit = models.CharField(max_length=200, null=True)
    qte_produit = models.IntegerField(default=0, null=True, blank=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)

    def __str__(self):
        return "Constituer#" + f"{self.id} "

    @property
    def get_total(self):
        total = self.produit.prix_achat * self.qte_produit
        return total
