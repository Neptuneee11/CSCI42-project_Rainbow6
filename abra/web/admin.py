from django.contrib import admin
from .models import Customer, Authentication, Bike, Transaction

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["Customer_ID", "Last_Name", "First_Name"]

class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ["Customer_ID", "Password"]

class BikeAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Authentication, AuthenticationAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Transaction, TransactionAdmin)
