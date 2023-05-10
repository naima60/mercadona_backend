from django.test import TestCase
from decimal import Decimal
from product.models import Produit, Promotion, Categorie
from datetime import date


# Create your tests here.
class ProdRemiseModelTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(libelle="Bien être")
        self.promotion = Promotion.objects.create(date_debut=date(2023, 5, 1), date_fin=date(2023, 5, 31), taux=25)
        self.produit = Produit.objects.create(libelle="Eau de parfum mujer My Soul Glacier",
                                              description="Frasco 100 ml | 12,00 €/100 ml", prix=12,
                                              category=self.categorie, promotions=self.promotion)
    def test_remise_calculation(self):
        prix_remise = self.produit.remise()
        # On s'attend à ce que le prix remisé soit égal à 9€
        self.assertEqual(prix_remise, Decimal('9.00'))


class ProdCategoryTestCase(TestCase):
    def setUp(self):
        # créer une instance de Categorie pour les tests
        self.categorie = Categorie.objects.create(libelle="Test categorie")

    def test_produit_creation(self):
        # Créer une instance de Produit avec la catégorie créée dans setUp()
        produit = Produit.objects.create(libelle="Test produit", prix=10.0, category=self.categorie)
        # Vérifier que l'objet Produit a été correctement créé en base de données
        self.assertEqual(produit.libelle, "Test produit")
        self.assertEqual(produit.prix, 10.0)
        self.assertEqual(produit.category, self.categorie)



