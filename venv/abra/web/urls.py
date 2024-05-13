from django.urls import path, include
from .views import index
from . import views

urlpatterns = [
    #path('', index, name='index'),
    path('web/', views.home, name="home"),
]

app_name = "web"