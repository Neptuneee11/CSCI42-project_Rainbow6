from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    return render(request, 'index.html', {'data': location_data})