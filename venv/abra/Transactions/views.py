from django.shortcuts import render, redirect
from .models import Transaction

# Create your views here.
def register(request):
    if request.method == "POST":
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data['customer'])

    return render(request)