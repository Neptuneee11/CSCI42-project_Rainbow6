from django.contrib import admin
from .models import UserProfile

# Register your models here.
#class UserAdmin(admin.ModelAdmin):
    #list_display = ["last_name", "first_name", "email", "id_number", "school_year", "course", "phone_number" ]

admin.site.register(UserProfile)