from django.db import models
from mamamboga.models import Mamamboga
# Create your models here.
class Product(models.Model):
    Mamamboga = models.ForeignKey(Mamamboga,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to="image/")
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
# Attribute stored in columns
# instance stored in rows