from django.urls import path

from .views import bicycleDetailView


urlpatterns = [
    #path('bicycles/', index, name='index'),
    path('bicycles/<int:pk>/details/', bicycleDetailView.as_view(), name='user-details'),
    #path('bicycles/add/', UserCreateView.as_view(), name='user-add'),
]

app_name = "bicycles"