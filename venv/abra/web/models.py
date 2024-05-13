from django.db import models
from django.contrib.auth.models import User

# client side data
class customerActions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    isRenting = models.BooleanField(default=False)
    charge = models.IntegerField(default=0)
    timeRenting = models.DurationField(default=0)