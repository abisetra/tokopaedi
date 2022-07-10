from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from toko.models.product import Product
from toko.models.cart import Cart
from django.contrib.auth.decorators import login_required

def addToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':'Produk sudah ada dalam keranjang', 'message':'Produk sudah ada dalam keranjang'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'Produk sukses ditambahkan', 'message':'Produk sukses ditambahkan'})
                    else:
                        return JsonResponse({'message':'Stok hanya tersisa ' + str(product_check.quantity)})
            else:
                return JsonResponse({ 'message':'Produk tidak ditemukan'})

        else:
            return JsonResponse({'status':'Login untuk melanjutkan'})
                    
    return redirect('/')
@login_required(login_url='login')
def cartView(request):
        cart = Cart.objects.filter(user=request.user.id)
        context = {'cart':cart}
        return render(request, 'toko/cart.html', context)


        

def updateCart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':'Keranjang berhasil diperbarui', 'message':'Keranjang berhasil diperbarui'})
    return redirect('/')

def deleteCartItem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.delete()
            return JsonResponse({'status':'Produk sukses dihapus dari keranjang', 'message':'Produk sukses dihapus dari keranjang'})
    return redirect('/') 