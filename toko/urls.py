import imp
from django.urls import URLPattern, path
from .views.collections import collections, collectionsView
from .views.home import home
from .views.product import productView
from .views.auth import register, login, logout
from .views.cart import addToCart, cartView, updateCart, deleteCartItem
from .views.wishlist import wishlistView, addToWishlist, deleteWishlistItem
from .views.checkout import checkoutView, placeorder

urlpatterns = [
    path('', home, name='home'),
    path('collections/', collections, name='collections'),
    path('collections/<str:slug>', collectionsView, name='collectionsView'),
    path('collections/<str:cate_slug>/<str:prod_slug>', productView, name='productView'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('add-to-cart', addToCart, name='addToCart'),
    path('cart', cartView, name='cart'),
    path('update-cart', updateCart, name='updatecart'),
    path('delete-cart-item', deleteCartItem, name='deletecartitem'),

    path('wishlist', wishlistView, name='wishlist'),
    path('add-to-wishlist', addToWishlist, name='addToWishlist'),
    path('delete-wishlist-item', deleteWishlistItem, name='deleteWishlistItem'),

    path ('checkout', checkoutView, name='checkout'),
    path ('place-order', placeorder, name='placeorder'),
]