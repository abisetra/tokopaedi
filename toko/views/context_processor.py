from toko.models.product import *
from toko.models.cart import *
from toko.models.checkout import *
from django.shortcuts import redirect, render
from django.contrib.auth.models import User



def global_cartcounter(request):
    if(request.user.id):
        return {
            'global_cartcounter': Cart.objects.filter(user=request.user.id).count()
        }
    return {
        'global_cartcounter':""
    }

def global_usercounter(request):
    if(request.user.id):
        return {
            'global_usercounter': User.objects.count()
        }
    return {
        'global_usercounter':""
    }

def global_prodcounter(request):
    if(request.user.id):
        return {
            'global_prodcounter': Product.objects.count()
        }
    return {
        'global_prodcounter':""
    }

def global_ordercounter(request):
    if(request.user.id):
        return {
            'global_ordercounter': Order.objects.count()
        }
    return {
        'global_ordercounter':""
    }