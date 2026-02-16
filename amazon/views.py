from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request,id):
    product=Product.object.get(id=id)
    return render(request, 'store/product_detail.html', {'product': product})
