from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=("amount","date_of_payment","payment_Status","receipt","payment_method")

admin.site.register(Payment, PaymentAdmin)