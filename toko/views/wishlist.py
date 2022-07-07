from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from toko.models.wishlist import Wishlist

@login_required(login_url='login')
def wishlistView(request):
    wishlistitems = Wishlist.objects.filter(user=request.user.id)
    context = {'wishlist':wishlistitems}
    return render(request, 'toko/wishlist.html', context)

