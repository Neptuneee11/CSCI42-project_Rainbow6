from django.db import models
from django.core.validators import RegexValidator
from bicycles.models import Bicycle
from Customer.models import UserProfile

# Create your models here.
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
    Customer_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()