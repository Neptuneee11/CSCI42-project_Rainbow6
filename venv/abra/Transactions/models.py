from django.db import models
from django.core.validators import RegexValidator
from bicycles.models import Bicycle
from django.contrib.auth.models import User

import datetime

# Create your models here.
# dsd
class Transaction(models.Model):
    Customer_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bicycle, on_delete=models.CASCADE)

    TYPES = {
        "RENT":"Rent",
        "RETURN":"Return",
    }

    transaction_type = models.CharField(choices=TYPES, max_length= 10, blank=False, default="RENT")
    transaction_time = models.DateTimeField(default=datetime.datetime.now)
    Duration = models.DurationField(default =datetime.timedelta(seconds=0, minutes=0, hours=0))
    Price = models.DecimalField(default=0, decimal_places=2, max_digits=12)