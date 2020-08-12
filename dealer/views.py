from django.shortcuts import render
from fpo.models import Product

# Create your views here.

def index_dealer(request):
    return render(request, 'dealer/index_dealer.html')


def fpoproducts(request):
    products = Product.objects.all().order_by('-datecreated')
    return render(request, 'dealer/products.html',{'products': products})