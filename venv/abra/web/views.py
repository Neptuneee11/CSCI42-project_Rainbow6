from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return render(request, "home.html")