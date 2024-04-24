from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20)
    school_year = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class PaymentInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    billing_address = models.TextField()

class LiabilityWaiver(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    waiver_accepted = models.BooleanField(default=False)

def get_absolute_url(self):
    return reverse('bicycles:bicycle-details', kwargs={'pk': self.pk})