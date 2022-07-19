from django.shortcuts import render


def patnolpat_view(request, exceptions):
    return render(request, '404.html', status=404)

def patnoltiga_view(request, exceptions):
    return render(request, '403.html', status=403)
