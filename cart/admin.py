from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display=("number","size")

admin.site.register(Cart, CartAdmin)