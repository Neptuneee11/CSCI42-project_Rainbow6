from django.urls import path
from .views import register

urlpatterns = [
    path('', register, name='transact'),
]

app_name = "transactions"