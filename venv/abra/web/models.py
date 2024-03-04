from django.db import models
import qrcode
from io import BytesIO
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
    Code = models.ImageField(blank=True, upload_to='Code')
    Bike_NO = models.CharField(max_length=255, primary_key=True)

    def __str__(self) -> str:
        return self.Bike_NO
    
    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.Bike_NO)
        qr_offset = Image.new('RGB', (310,310), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.Bike_NO}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.Code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args,**kwargs)

    
class Transaction(models.Model):
    Transaction_NO = models.CharField(max_length=255, primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Bike_NO = models.ForeignKey(Bike, on_delete=models.CASCADE)
    Duration = models.IntegerField()
    Price = models.IntegerField()