from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Transaction
from bicycles.models import Bicycle
from web.models import customerActions
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import math


# Create your views here.
def logPage(request):
    if request.method == "POST":
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        customer_username = post_data['customer']
        bicycle_link = post_data['bicycle']
        transaction_type = post_data['action']

        #extract bicycle ID from link   
        #http://localhost:8000/bicycles/1/details/

        #single out the pkey from the link
        bicycle_pkey = ""
        exttt = 0
        leChar = ""
        while leChar != "/":
            leChar = bicycle_link[bicycle_link.find("/bicycles/")+len("/bicycles/")+exttt]
            print(leChar)
            exttt+=1
            bicycle_pkey+=leChar

        if transaction_type == "Rent":
            Transaction.objects.create(
                Customer_ID = request.user,
                Bike_NO = Bicycle.objects.get(pk=bicycle_pkey[:-1]),
                transaction_type = "RENT",
            )
            
        elif transaction_type == "Return":
            def rentRate(dur):
                #resolution is 5 mins
                mins = dur/datetime.timedelta(minutes=5)

                # first 30 mins have a flat rate of 15 pesos
                if (mins <= 6):
                    return 15
                
                # every 5 min extension adds 5 pesos to the bill
                else:
                    mins = mins-6
                    ans = math.ceil(mins*5)
                    return ans

            Transaction.objects.create(
                Customer_ID = request.user,
                Bike_NO = Bicycle.objects.get(pk=bicycle_pkey[:-1]),
                Duration = timezone.now() - request.user.profile.time_since_last_rent,
                Price = rentRate(timezone.now() - request.user.profile.time_since_last_rent),
                transaction_type = "RETURN",
            )

            # add to the customer's bill
            thisCust = customerActions.objects.get(userConnected=request.user)
            thisCust.charge += rentRate(timezone.now() - request.user.profile.time_since_last_rent)
            thisCust.save()
    
    return HttpResponse("Thank")
