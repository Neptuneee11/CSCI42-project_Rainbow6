from django.db import models
from django.core.validators import RegexValidator
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
    
# dsd
class Transaction(models.Model):
    Transaction_NO = models.CharField(
        max_length=7,
        validators=[
            RegexValidator(
                regex=r'^TN-\d{2}$',
                message="Transaction number is invalid. Not in the format TN-XX.",
                code="invalid_transaction_number"
            )
        ])
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bike, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()