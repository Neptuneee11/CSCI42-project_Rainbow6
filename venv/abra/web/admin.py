from django.contrib import admin
from .models import Customer, Authentication, Bike, Transaction

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["Customer_ID", "Last_Name", "First_Name"]

class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ["Customer_ID", "Password"]

class BikeAdmin(admin.ModelAdmin):
    list_display = ["Bike_NO"]

class TransactionAdmin(admin.ModelAdmin):
    list_display = ["Transaction_NO", "Duration", "Price"]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Authentication, AuthenticationAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Transaction, TransactionAdmin)
