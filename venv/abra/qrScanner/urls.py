from django.urls import path
from .views import qrScan

urlpatterns = [
    path('', qrScan, name='qrScan'),
]

app_name = "qrScanner"