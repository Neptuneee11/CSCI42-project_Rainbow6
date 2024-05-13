from django.db import models
from django.core.validators import RegexValidator
from django_fsm import FSMField, transition
from django.urls import reverse

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
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bike, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()