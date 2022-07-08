from django.shortcuts import HttpResponse, render 
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from toko.models.checkout import *


def orders(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'toko/orders/index.html', context)

def orderView(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, 'toko/orders/view.html', context)