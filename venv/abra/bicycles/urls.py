from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('bicycles/<int:pk>/details/', UserDetailView.as_view(), name='user-details'),
    #path('bicycles/add/', UserCreateView.as_view(), name='user-add'),
]

app_name = "bicycles"