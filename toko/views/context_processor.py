from toko.models.product import *
from toko.models.cart import Cart
from django.shortcuts import redirect, render

def global_cartcounter(request):
    if(request.user.id):
        return {
            'global_cartcounter': Cart.objects.filter(user=request.user.id).count()
        }
    return {
        'global_cartcounter':""
    }