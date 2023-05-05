from django.contrib import admin

from product.models import Categorie, Promotion, Produit


# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('libelle', 'active')

admin.site.register(Categorie, AdminCategorie)

class AdminPromotion(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'taux')

admin.site.register(Promotion, AdminPromotion)


class AdminProduit(admin.ModelAdmin):
    list_display = ('libelle', 'description', 'prix', 'remise','category', 'active')


admin.site.register(Produit, AdminProduit)

