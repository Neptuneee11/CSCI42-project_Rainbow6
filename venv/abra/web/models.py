from django.db import models
from bicycles.models import Bicycle

class Customer(models.Model):
    Customer_ID = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)


class Authentication(models.Model):
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Password = models.CharField(max_length=255, primary_key=True)
    

class Transaction(models.Model):
    Transaction_NO = models.CharField(max_length=255, primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()