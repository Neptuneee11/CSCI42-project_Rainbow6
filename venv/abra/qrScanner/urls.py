from django.urls import path
from .views import qrScan_Rent, qrScan_Return

urlpatterns = [
    path('rent/', qrScan_Rent, name='qrScan_Rent'),
    path('return/', qrScan_Return, name='qrScan_Return'),
]

app_name = "qrScanner"