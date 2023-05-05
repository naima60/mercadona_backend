from django.shortcuts import render
from product.models import Produit

# Create your views here.
def index(request):
    # products = Produit.objects.all()
    products = Produit.objects.filter(active='True')
    return render(request, 'produit/index.html', context={"products": products})


