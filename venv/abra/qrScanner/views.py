from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def qrScan_Rent(request):
    context = {
        "User": User,
    }
    return render(request, 'qrScanner/qrRent.html',context)

def qrScan_Return(request):
    return render(request, 'qrScanner/qrReturn.html')

def qrScan(request):
    return render(request, 'qrScanner/qrGET.html')