from django.db import models
from .category import Category
import os
import datetime


# Create your models here.

def get_file_path_products(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/products/', filename)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path_products, null=True, blank=True)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.DecimalField(default=0, null=False, blank=False, decimal_places=2, max_digits=10)
    selling_price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    tag = models.CharField(max_length=100, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

