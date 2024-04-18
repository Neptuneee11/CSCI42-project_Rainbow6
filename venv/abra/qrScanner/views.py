from django.shortcuts import render

# Create your views here.
def qrScan(request):
    return render(request, 'qrScanner/qrIndex.html')