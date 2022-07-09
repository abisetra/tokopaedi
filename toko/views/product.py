from email import message
from django.shortcuts import redirect, render
from django.views import View
from toko.models.category import Category
from django.contrib import messages

from toko.models.product import Product


def productView(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products':products}
        else:
            sweetify.error(request, 'Products not found')
            return redirect('collections')
        
    else:
        sweetify.error(request, 'Category not found')
        return redirect('collections')
    return render(request, 'toko/products/view.html', context)