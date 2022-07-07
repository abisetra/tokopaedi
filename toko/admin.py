from django.contrib import admin

from toko.models.category import *
from toko.models.checkout import Order, OrderItem
from toko.models.product import *
from toko.models.cart import *
from toko.models.user import *
from toko.models.checkout import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)