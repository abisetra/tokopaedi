from email import message
from email.mime import image
from pyexpat import model
from unicodedata import category
from django.db import models
from .product import Product
from .user import User
import os
import datetime

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_depan = models.CharField(max_length=150, null=False, blank=False)
    nama_belakang = models.CharField(max_length=150, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    ponsel = models.IntegerField(null=False, blank=False)
    alamat = models.CharField(max_length=150, null=False, blank=False)
    kota = models.CharField(max_length=150, null=False, blank=False)
    provinsi = models.CharField(max_length=150, null=False, blank=True)
    kode_pos = models.CharField(max_length=150, null=False, blank=False)
    total_price = models.IntegerField(null=False, blank=False)
    payment_mode = models.CharField(max_length=150, null=False, blank=True)
    payment_id = models.CharField(max_length=250, null=False, blank=False)
    password = models.CharField(max_length=250, null=False, blank=False)
    orderstatus = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=150, null=False, choices=orderstatus, default='Pending')
    message = models.TextField(null=True, blank=True)
    tracking_no = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)