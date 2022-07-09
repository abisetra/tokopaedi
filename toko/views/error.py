from django.shortcuts import render


def patnolpat_view(request):
    return render(request, '403.html', status=404)

def patnoltiga_view(request):
    return render(request, '403.html', status=404)
