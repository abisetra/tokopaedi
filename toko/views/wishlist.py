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
                    return JsonResponse({'status':'Produk sudah ada dalam Wishlist', 'message':'Produk sudah ada dalam Wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'Produk ditambahkan ke wishlist', 'message':'Produk ditambahkan ke wishlist'})
            else:
                return JsonResponse({'status':'Produk tidak ditemukan', 'message':'Produk tidak ditemukan'})
        else:
            return JsonResponse({'status':'Login untuk melanjutkan', 'message':'Login untuk melanjutkan'})
    return redirect('/')

def deleteWishlistItem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':'Product dihapus dari Wishlist', 'message':'Product dihapus dari Wishlist'})
            else:
                return JsonResponse({'status':'Produk tidak ditemukan', 'message':'Produk tidak ditemukan'})
        else:
            return JsonResponse({'status':'Login untuk melanjutkan', 'message':'Login untuk melanjutkan'})
    return redirect('/')

