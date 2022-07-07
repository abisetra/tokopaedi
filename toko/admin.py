from django.contrib import admin

from toko.models.category import *
from toko.models.product import *
from toko.models.cart import *
from toko.models.user import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)