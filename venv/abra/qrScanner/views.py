from django.shortcuts import render

# Create your views here.
def qrScan_Rent(request):
    return render(request, 'qrScanner/qrRent.html')

def qrScan_Return(request):
    return render(request, 'qrScanner/qrReturn.html')