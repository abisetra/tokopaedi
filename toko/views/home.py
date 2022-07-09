from multiprocessing import context
from django.shortcuts import render
from toko.models.product import *

# Create your views here.

def home(request):
    trending_products = Product.objects.filter(trending=1)
    all_products = Product.objects.filter(status=0)
    context = {'trending_products':trending_products, 'all_products':all_products}
    return render(request, 'toko/index.html', context)