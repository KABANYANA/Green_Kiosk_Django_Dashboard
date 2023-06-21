from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    location = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    def __str__(self):
        return self.name