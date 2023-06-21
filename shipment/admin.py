from django.contrib import admin

# Register your models here.
from .models import Shipment

class ShipmentAdmin(admin.ModelAdmin):
    list_display=("port_name","date_of_shipment","date_of_arrival","product_name","delivery_person")

admin.site.register(Shipment, ShipmentAdmin)