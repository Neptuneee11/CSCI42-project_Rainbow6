from django.db import models
from django_fsm import FSMField, transition
from django.urls import reverse

# Create your models here.
class Bicycle(models.Model):
    # available, rented, under maintenance
    state = FSMField(default = "available", protected = True)
    STATIONS = {
    "Bellarmine",
    "Matteo Ricci",
    "Leong",
    "CTC",
    "Seminary",
    }
    location = models.CharField(choices = STATIONS, blank = False)

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
    
