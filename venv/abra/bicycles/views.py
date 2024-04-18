from django.views.generic.detail import DetailView

from .models import Bicycle

# Create your views here.
class bicycleDetailView(DetailView):
    model = Bicycle
    template_name = 'bicycles/bicycle-details.html'