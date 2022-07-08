from django.contrib import admin

from toko.models.category import *
from toko.models.checkout import *
from toko.models.product import *
from toko.models.cart import *
from toko.models.user import *
from toko.models.checkout import *
from toko.models.profile import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)