from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.tailor = request.user
            product.save()
            return redirect(products)
    return render(request,'products/create_product.html',context={'form':form})

@login_required
def products(request):
    products = Product.objects.filter(tailor=request.user)
    return render(request,'products/products.html',context={'products':products})