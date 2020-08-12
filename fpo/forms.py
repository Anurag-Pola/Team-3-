from django.forms import ModelForm
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields=['productname','description','quantity','expectedprice']
