from django.db import models
from django_fsm import FSMField, transition

# Create your models here.
class Bicycle(models.Model):
    # available, rented, under maintenance
    state = FSMField(default = "available", protected = True)
    location = {
    "Bellarmine",
    "Matteo Ricci",
    "Leong",
    "CTC",
    "Seminary",
    }

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
    
