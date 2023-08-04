from django.db import models
from django.contrib.auth.models import User
from orders.models import Orders

    
# Create your models here.
class Customers(models.Model):
    Orders= models.ForeignKey(Orders,on_delete=models.PROTECT)
    User= models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    location = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __str__(self):
        return self.name