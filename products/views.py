from django.shortcuts import render

from products.models import Products, ProductCategory
import pickle
import datetime


def index(request):
    context = {
        'title': 'GeekShop',
        'date': datetime.datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    products_from_sql = Products.objects.values_list('image', 'name', 'price', 'short_description')
    convert_to_list_dict = Products.objects.all()
    convert_to_list_dict.query = pickle.loads(pickle.dumps(products_from_sql.query))

    context = {
        'title': 'Products',
        'h1_geekShop': 'geekShop',
        'product': convert_to_list_dict,
    }
    return render(request, 'products/products.html', context)
