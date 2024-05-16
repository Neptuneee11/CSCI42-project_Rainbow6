from django.urls import path

from .views import bicycleDetailView, bicycleListView


urlpatterns = [
    path('', bicycleListView.as_view(), name='bicycle-list'),
    path('<int:pk>/details/', bicycleDetailView, name='bicycle-details'),
    #path('bicycles/add/', UserCreateView.as_view(), name='user-add'),
]

app_name = "bicycles"