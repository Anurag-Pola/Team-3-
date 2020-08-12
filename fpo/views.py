from django.shortcuts import render,redirect
from . forms import ProductForm
from . models import Product
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from accounts.models import Fpo, User
from django.db import IntegrityError
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

# Create your views here.

def index_fpo(request):
    return render(request, 'fpo/index_fpo.html')


class ProductCreateView(CreateView):
    model = Product
    form_class=ProductForm
    template_name = 'fpo/createproduct.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.fpo = self.request.user.fpo
        product.save()
        return redirect('fpo:index_fpo')


def allproducts(request):
    products= Product.objects.filter(fpo = request.user.fpo)
    return render(request,'fpo/allproducts.html',{'products':products})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'fpo/updateproduct.html'

    def get_queryset(self):
        return self.request.user.fpo.product.all()
    
    def get_success_url(self):
        return reverse('fpo:allproducts')

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'fpo/deleteproduct.html'
    success_url = reverse_lazy('fpo:allproducts')

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.fpo.product.all()