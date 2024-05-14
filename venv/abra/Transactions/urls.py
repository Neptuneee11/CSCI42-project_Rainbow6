from django.urls import path
from .views import logPage

urlpatterns = [
    path('', logPage, name='transact'),
]

app_name = "transactions"