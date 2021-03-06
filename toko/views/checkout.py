from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.contrib.auth.decorators import login_required

from toko.models.cart import *
from toko.models.checkout import *
from toko.models.product import *
from toko.models.profile import *
from toko.models.user import *
from django.contrib.auth.models import User
import sweetify

import random

@login_required(login_url='login')
def checkoutView(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.filter(id=item.id).delete()
            return JsonResponse({'status':'Only ' + str(item.product.quantity) +" quantity available", 'message':'Product Quantity is not available'})
            
    
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price += total_price + item.product.selling_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()


    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile}
    return render(request, 'toko/checkout.html', context)

@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name :
            currentuser.first_name = request.POST.get ('nama_depan')
            currentuser.last_name = request.POST.get('nama_belakang')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.ponsel = request.POST.get('ponsel')
            userprofile.alamat = request.POST.get('alamat')
            userprofile.kota = request.POST.get('kota')
            userprofile.provinsi = request.POST.get('provinsi')
            userprofile.kode_pos = request.POST.get('kode_pos')
            userprofile.password = request.POST.get('password')
            userprofile.save()


        neworder = Order()
        neworder.user = request.user
        neworder.nama_depan = request.POST.get('nama_depan')
        neworder.nama_belakang = request.POST.get('nama_belakang')
        neworder.email = request.POST.get('email')
        neworder.ponsel = request.POST.get('ponsel')
        neworder.alamat = request.POST.get('alamat')
        neworder.kota = request.POST.get('kota')
        neworder.provinsi = request.POST.get('provinsi')
        neworder.kode_pos = request.POST.get('kode_pos')
        neworder.password = request.POST.get('password')
       
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'XPRS'+str(random.randint(111111111,999999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'XPRS'+str(random.randint(111111111,999999999))

        pay_id = str(random.randint(111111111,999999999))
        while Order.objects.filter(payment_id=pay_id) is None:
            pay_id = str(random.randint(111111111,999999999))

        
        neworder.payment_id = pay_id
        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                quantity=item.product_qty,
                price=item.product.selling_price
            )
            
            #Mengurangi product quantity dari stok gudang
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        #untuk membersihkan cart user
        Cart.objects.filter(user=request.user).delete()

        sweetify.success(request, 'Pesanan berhasil ditambahkan', button='OK', timer=2000)

        payMode = request.POST.get('payment_mode')
        if (payMode) == "Paid by Paypal":
            return JsonResponse({'status':'Pesanan berhasil ditambahkan'})
    return redirect('/')

