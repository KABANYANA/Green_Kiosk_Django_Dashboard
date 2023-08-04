from django.db import models
from payment.models import Payment
# Create your models here.
class Orders(models.Model):
    Payment = models.OneToOneField(Payment,on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=32, default='Default Order Name')
    placement_date = models.DateTimeField(auto_now_add=True)
    order_Status = models.CharField(max_length=32)
    number_of_Orders = models.PositiveIntegerField()
    total_amount = models.IntegerField()
    def __str__(self):
        return self.name