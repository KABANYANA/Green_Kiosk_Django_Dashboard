from django.contrib import admin

# Register your models here.
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display=("sender_name","title","description","message","time")

admin.site.register(Notification,NotificationAdmin)