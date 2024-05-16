from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import customerActions
from django.utils import timezone
from datetime import datetime
from bicycles.models import Bicycle
from Transactions.models import Transaction

def index(request):
    return render(request, 'index.html')

def home(request):
    currentCustomer = customerActions.objects.get(userConnected=request.user)

    charge = Transaction.objects.filter(Customer_ID=request.user).aggregate(Sum("Price"))

    print("THIS CUSTOMER OWES US " + str(charge["Price__sum"]) + "Pesos")

    thisCust = customerActions.objects.get(userConnected=request.user)

    thisCust.charge = charge["Price__sum"]
    thisCust.save()

    if request.method == "POST":
        print("YIPEEEE")
        import json
        post_data = json.loads(request.body.decode("utf-8"))

        currentCustomer.isRenting = post_data['currentlyRenting']
        bicycle_link = post_data['currentBicycle']
        
        if currentCustomer.isRenting:
            #single out the pkey from the link
            bicycle_pkey = ""
            exttt = 0
            leChar = ""
            while leChar != "/":
                leChar = bicycle_link[bicycle_link.find("/bicycles/")+len("/bicycles/")+exttt]
                print(leChar)
                exttt+=1
                bicycle_pkey+=leChar

            currentCustomer.time_since_last_rent = timezone.now()
            currentCustomer.currentlyRenting = Bicycle.objects.get(pk=bicycle_pkey[:-1])

        else:
            currentCustomer.time_since_last_rent = None
            currentCustomer.currentlyRenting = None

        currentCustomer.save()
    
    if request.method == "GET":
        pass


    context = {
        "rentStatus" : currentCustomer.isRenting,
        "timeStartRent" : currentCustomer.time_since_last_rent,
    }

    return render(request, "home.html", context)

def logout_view(request):
    logout(request)
    return render(request, "home.html")