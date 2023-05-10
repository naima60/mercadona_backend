from django.db import models
from decimal import Decimal
from django.db.models.signals import pre_save
from django.dispatch import receiver




class Categorie(models.Model):
    libelle = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    # la fonction __str__ permet d'afficher le nom de l'objet créé dans admin Django
    def __str__(self):
        return self.libelle


class Promotion(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    taux = models.FloatField(null=True)

class Produit(models.Model):
    libelle = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    prix = models.FloatField(null=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    promotions = models.ForeignKey('Promotion', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.libelle

    def remise(self):
        if self.promotions and self.promotions.taux:
            remise = Decimal(str(self.prix)) * Decimal(str(self.promotions.taux)) / 100
            prix_remise = Decimal(str(self.prix)) - remise
            return round(Decimal(str(prix_remise)),2)
        else:
            prix_remise = round(self.prix, 2)


