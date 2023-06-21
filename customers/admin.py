from django.contrib import admin

# Register your models here.
from .models import Customers

class CustomersAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_Number","location","password")

admin.site.register(Customers, CustomersAdmin)