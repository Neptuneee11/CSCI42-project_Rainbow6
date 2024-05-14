from django.db import models
from django.contrib.auth.models import User
import datetime

# client side data
class customerActions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    isRenting = models.BooleanField(default=False)
    charge = models.IntegerField(default=0)
    timeRenting = models.DurationField(default=datetime.timedelta(seconds=0, minutes=0, hours=0))

    def __str__(self):
        return self.user.username