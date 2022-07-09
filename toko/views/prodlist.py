from itertools import product
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render 
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from toko.models.product import Product
import sweetify

def productList(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productsList = list(products)

    return JsonResponse(productsList, safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()

            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                sweetify.info(request, 'Product not found')
                return redirect(request.META.get('HTTP_REFERER')) 



    return redirect(request.META.get('HTTP_REFERER'))
   