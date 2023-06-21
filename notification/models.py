from django.db import models

# Create your models here.
class Notification(models.Model):
    sender_name = models.CharField(max_length=32)
    title = models.CharField(max_length=86)
    description = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name