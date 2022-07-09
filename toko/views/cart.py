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
                    return JsonResponse({'status':'Product Already in Cart', 'message':'Product Already in Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'Product added Successfully', 'message':'Product added Successfully'})
                    else:
                        return JsonResponse({'status':'Only ' + str(product_check.quantity) +" quantity available", 'message':'Product Quantity is not available'})
            else:
                return JsonResponse({'status':'error', 'message':'Product not found'})

        else:
            return JsonResponse({'status':'Login to Continue', 'message':'You are not logged in'})
                    
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
            return JsonResponse({'status':'Product Updated Successfully', 'message':'Product Updated Successfully'})
    return redirect('/')

def deleteCartItem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.delete()
            return JsonResponse({'status':'Product Deleted Successfully', 'message':'Product Deleted Successfully'})
    return redirect('/') 