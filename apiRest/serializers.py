from rest_framework import serializers
from product.models import Produit, Categorie

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    remise = serializers.SerializerMethodField()
    class Meta:
        model = Produit
        fields = ('id','libelle', 'description', 'prix', 'remise','image', 'category', 'active')

    def get_remise(self, obj):
        return obj.remise()