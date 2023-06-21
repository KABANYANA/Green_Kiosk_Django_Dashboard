from django.contrib import admin

# Register your models here.
from .models import Delivery_person

class Delivery_personAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_Number","location")

admin.site.register(Delivery_person, Delivery_personAdmin)