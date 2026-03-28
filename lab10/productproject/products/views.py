from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'products/add_product.html', {'form': form})