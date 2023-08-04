from django.db import models
from inventory.models import Product
from orders.models import Orders
# Create your models here.
class Cart(models.Model):
    Orders= models.ForeignKey(Orders,on_delete=models.PROTECT)
    Product=models.ManyToManyField(Product)
    number = models.PositiveIntegerField
    size = models.PositiveIntegerField()
    def __str__(self):
        return self.number
   
