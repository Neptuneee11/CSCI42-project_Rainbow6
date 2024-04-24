from django.contrib import admin
from .models import Customer, PaymentInfo, LiabilityWaiver

# Register your models here.
class customerAdmin(admin.ModelAdmin):
    model = Customer

    list_display = ('id', 'full_name', 'school_year','course', 'phone_number','email')
    search_fields = ('id', 'full_name', 'school_year','course')
    list_filter = ('id', 'full_name', 'school_year','course',)

class paymentinfoAdmin(admin.ModelAdmin):
    model = PaymentInfo

    list_display = ('customer', 'payment_method', 'billing_address')
    search_fields = ('customer', 'payment_method', 'billing_address')
    list_filter = ('customer', 'payment_method', 'billing_address')

class liabilityAdmin(admin.ModelAdmin):
    model = LiabilityWaiver

    list_display = ('customer', 'waiver_accepted')
    search_fields = ('customer')
    list_filter = ('customer', 'waiver_accepted')
    
admin.site.register(Customer, customerAdmin)
admin.site.register(PaymentInfo, paymentinfoAdmin)
admin.site.register(LiabilityWaiver, liabilityAdmin)
