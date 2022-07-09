
from django.shortcuts import redirect, render
from toko.models.category import Category
from toko.models.product import Product
from django.contrib import messages
import sweetify

# Create your views here.

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, 'toko/collections.html', context)

def collectionsView(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request, 'toko/products/index.html', context)
    else:
        sweetify.error(request, 'Category not found')
        return redirect('collections')
        