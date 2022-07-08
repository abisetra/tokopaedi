from multiprocessing import context
from django.shortcuts import render
from toko.models.product import *

# Create your views here.

def home(request):
    trending_products = Product.objects.filter(trending=1)
    context = {'trending_products':trending_products}
    return render(request, 'toko/index.html', context)