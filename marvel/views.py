from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

from .models import Character, Comic

def characters(request):
    chars = Character.objects.all()
    return render(request, 'charaters.html', {'characters': chars})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Hero Identity or encryption key.")
            
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Encryption keys do not match.")
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "That Hero Identity has already been claimed.")
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        auth_login(request, user)
        messages.success(request, "Welcome to the Avengers Initiative, Hero!")
        return redirect('home')

    return render(request, 'register.html')

def logout_view(request):
    auth_logout(request)
    messages.info(request, "Logged out of S.H.I.E.L.D. Secure Network.")
    return redirect('login')

def password(request):
    return render(request, 'password.html')

def cm(request):
    comics_list = Comic.objects.all()
    return render(request, 'cm.html', {'comics': comics_list})
