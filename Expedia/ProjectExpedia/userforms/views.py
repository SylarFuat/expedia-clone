from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserFormCreate, UserFormLogin

# Create your views here.
def login_view(request):
    form = UserFormLogin()
    if request.method =='POST':
        form = UserFormLogin(request.POST)
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Log in successfull!")
                return redirect('home')

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserFormCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created your account!")
            return redirect('login_view')
        else:
            messages.error(request, 'Invalid username or password. Try again!')
    else:
        form = UserFormCreate()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
