from django.db import models

# Create your models here.
class Review(models.Model):
    sender_name = models.CharField(max_length=32)
    time_and_date = models.DateField(auto_now_add=True)
    message = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name