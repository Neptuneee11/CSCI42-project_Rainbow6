from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # Add other URL patterns here
]

app_name = "Customer"