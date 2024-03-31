from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw

class Customer(models.Model):
    Customer_ID = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)


class Authentication(models.Model):
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Password = models.CharField(max_length=255, primary_key=True)


class Bike(models.Model):
    id = models.AutoField()

    def __str__(self) -> str:
        return self.id
    

class Transaction(models.Model):
    Transaction_NO = models.CharField(max_length=255, primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bike, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()