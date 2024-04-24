from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    customer = Customer.objects.all()
    return render(request, 'customer/customer-list.html', {'customer': customer,})

class bicycleDetailView(DetailView):
    model = Customer
    template_name = 'bicycles/bicycle-details.html'