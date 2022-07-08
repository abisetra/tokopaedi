from django.shortcuts import render

# Create your views here.

def qrisView(request):
    return render(request, 'toko/qris.html')