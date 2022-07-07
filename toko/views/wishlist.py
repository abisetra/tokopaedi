from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from toko.models.wishlist import Wishlist
from toko.models.product import Product

@login_required(login_url='login')
def wishlistView(request):
    wishlistitems = Wishlist.objects.filter(user=request.user.id)
    context = {'wishlist':wishlistitems}
    return render(request, 'toko/wishlist.html', context)

def addToWishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if(Wishlist.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':'Product Already in Wishlist', 'message':'Product Already in Wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'Product added to wishlist', 'message':'Product added to wishlist'})
            else:
                return JsonResponse({'status':'Product not found', 'message':'Product not found'})
        else:
            return JsonResponse({'status':'Login to continue', 'message':'Login to continue'})
    return redirect('/')

def deleteWishlistItem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':'Product Deleted Successfully', 'message':'Product Deleted Successfully'})
            else:
                return JsonResponse({'status':'Product not found', 'message':'Product not found'})
        else:
            return JsonResponse({'status':'Login to continue', 'message':'Login to continue'})
    return redirect('/')

