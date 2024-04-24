from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import bicycleForm

from .models import Bicycle

# Create your views here.
def bicycleDetailView(request, pk):

    bicy = Bicycle.objects.get(pk=pk)

    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data['state'])
        print(post_data['location'])

        bicy.state = post_data['state']
        bicy.location = post_data['location']

        bicy.save()
        
    return render(request,'bicycles/bicycleDetail.html', {'object' : bicy})


class bicycleListView(ListView):
    model = Bicycle
    template_name = 'bicycles/bicycleList.html'