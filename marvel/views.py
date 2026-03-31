from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def characters(request):
    return render(request, 'charaters.html')

def login(request):
    return render(request, 'login.html')

def password(request):
    return render(request, 'password.html')

def cm(request):
    return render(request, 'cm.html')
