from django.shortcuts import render
from django.http import HttpResponse
from.models import Bike
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, "home.html")

def bike(request):
    return render(request, 'bike_view.html')

class BikeListView(ListView):
    template_name = 'bike_list.html'
    queryset = Bike.objects.all()