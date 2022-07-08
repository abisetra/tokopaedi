from email import message
from email.mime import image
from pyexpat import model
from unicodedata import category
from django.db import models
from .product import Product
from .user import User
import os
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ponsel = models.IntegerField(null=False, blank=False)
    alamat = models.CharField(max_length=150, null=False, blank=False)
    kota = models.CharField(max_length=150, null=False, blank=False)
    provinsi = models.CharField(max_length=150, null=False, blank=True)
    kode_pos = models.CharField(max_length=150, null=False, blank=False)
    password = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username