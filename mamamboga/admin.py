from django.contrib import admin

# Register your models here.
from .models import Mamamboga

class MamambogaAdmin(admin.ModelAdmin):
    list_display=("name","email","phone_Number","location","password")

admin.site.register(Mamamboga, MamambogaAdmin)