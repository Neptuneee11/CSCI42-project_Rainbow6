from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method == "POST":
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data['currentlyRenting'])


    context = {

    }
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return render(request, "home.html")