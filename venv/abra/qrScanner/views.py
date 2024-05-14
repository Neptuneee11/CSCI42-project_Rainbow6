from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def qrScan_Rent(request):
    context = {
        "User": request.user,
    }
    return render(request, 'qrScanner/qrRent.html',context)

def qrScan_Return(request):
    
    context = {
        "User": request.user,
        "rentedBike": request.user.profile.currentlyRenting.get_absolute_url(),
    }
    print(context["rentedBike"])
    return render(request, 'qrScanner/qrReturn.html',context)

def qrScan(request):
    return render(request, 'qrScanner/qrGET.html')