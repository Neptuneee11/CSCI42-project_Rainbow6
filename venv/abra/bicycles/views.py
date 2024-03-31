from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Bicycle

# Create your views here.
def index(request):
    bicycle = Bicycle.objects.all()
    return render(request, 'bicycles/bicycle-list.html', {'bicycle': bicycle,})

class bicycleDetailView(DetailView):
    model = Bicycle
    template_name = 'bicycles/bicycle-details.html'