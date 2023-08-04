from django.db import models

from orders.models import Orders

    

# Create your models here.
class Shipment(models.Model):

    Orders= models.ForeignKey(Orders,on_delete=models.PROTECT)
    port_name = models.CharField(max_length=64)
    date_of_shipment = models.DateTimeField(auto_now_add=True)
    date_of_arrival = models.DateTimeField(auto_now=True)
    product_name = models.CharField(max_length=32)
    delivery_person = models.CharField(max_length=32)
    def __str__(self):
        return self.name