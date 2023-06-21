from django.contrib import admin

# Register your models here.
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display=("name","placement_date","number_of_Orders","total_amount","order_Status")
admin.site.register(Orders, OrdersAdmin)