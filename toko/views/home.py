from django.shortcuts import render
from toko.models.product import *

# Create your views here.

def home(request):
    trending_products
    return render(request, 'toko/index.html')