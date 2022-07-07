from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from toko.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered, Login to continue')
            return HttpResponseRedirect('/login/')
    context = {'form':form}
    return render(request, 'toko/auth/register.html', context)

def login(request):
    if request.user.is_authenticated:
     messages.success(request, 'You are already logged in')
     return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/login/')
        return render(request, 'toko/auth/login.html')

def logout(request):
    if request.user.is_authenticated:
        user_logout(request)
        messages.success(request, 'Logged out Successfully')
        return redirect('/')
    else:
        messages.error(request, 'You are not logged in')
        return redirect('/login/')