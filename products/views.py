from django.shortcuts import render

from products.models import Products, ProductCategory
import datetime


def index(request):
    context = {
        'title': 'GeekShop',
        'date': datetime.datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    products = Products.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'title': 'Products',
        'h1_geekShop': 'geekShop',
        'product': products,
        'category': categories
    }
    return render(request, 'products/products.html', context)
