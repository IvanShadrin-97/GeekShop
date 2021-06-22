from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Products, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'Products',
        'h1_geekShop': 'geekShop',
        'category': ProductCategory.objects.all()
    }
    products =  Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    context['product'] = products_paginator
    return render(request, 'products/products.html', context)
