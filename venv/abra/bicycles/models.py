from django.db import models
from django_fsm import FSMField, transition
from django.urls import reverse

# Create your models here.
class Bicycle(models.Model):
    # available, rented, under maintenance
    state = FSMField(default = "available", protected = False)
    STATIONS = {
        "BEL":"Bellarmine",
        "MACCI":"Matteo Ricci",
        "LEO":"Leong",
        "CTC":"CTC",
        "SEM":"Seminary",
    }
    
    location = models.CharField(max_length = 90, choices = STATIONS, blank = False)

    @transition(field=state, source="available", target="in_use")
    def getRented(self):
        pass
    @transition(field=state, source="in_use", target="available")
    def getReturned(self):
        pass
    @transition(field=state, source="available", target="maintenance")
    def getRepaired(self):
        pass
    @transition(field=state, source="maintenance", target="available")
    def doneRepair(self):
        pass

    def get_absolute_url(self):
        return reverse('bicycles:bicycle-details', kwargs={'pk': self.pk})
    
