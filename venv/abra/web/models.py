from django.db import models
from django.contrib.auth.models import User
from bicycles.models import Bicycle
import datetime

# client side data
class customerActions(models.Model):
    userConnected = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    isRenting = models.BooleanField(default=False)
    currentlyRenting = models.OneToOneField(Bicycle, on_delete=models.SET_NULL, null=True, blank=True)
    charge = models.IntegerField(default=0)
    time_since_last_rent = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return self.userConnected.username