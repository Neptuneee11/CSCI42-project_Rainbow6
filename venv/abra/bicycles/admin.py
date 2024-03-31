from django.contrib import admin
from .models import Bicycle

class bicycleAdmin(admin.ModelAdmin):
    model = Bicycle

    list_display = ('id', 'state', 'location')
    search_fields = ('state', 'location')
    list_filter = ('state', 'location')

# Register your models here.
admin.site.register(Bicycle, bicycleAdmin)
