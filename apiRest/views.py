from rest_framework.viewsets import ReadOnlyModelViewSet
from product.models import Categorie, Produit
from apiRest.serializers import CategorySerializer, ProductSerializer

class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Categorie.objects.filter(active=True)

class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
            category = self.request.query_params.get('category')
            queryset = Produit.objects.filter(active=True)
            if category:
                queryset = queryset.filter(category=category)
            return queryset
