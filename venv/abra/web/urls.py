from django.urls import path, include
from .views import index
from . import views
from .views import BikeListView

urlpatterns = [
    #path('', index, name='index'),
    path('', views.home, name="home"),
    path('bike/', BikeListView.as_view(), name='bike-view'),
]

app_name = "web"