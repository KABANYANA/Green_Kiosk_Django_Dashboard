from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.IntegerField
    date_of_payment = models.DateTimeField(auto_now_add=True)
    payment_Status = models.BooleanField()
    receipt = models.CharField(max_length=32)
    payment_method = models.CharField(max_length=32)
    def __str__(self):
        return self.name