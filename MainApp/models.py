from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    message = models.CharField(max_length=1000000)
    room_id = models.IntegerField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    username = models.CharField(max_length=1000)
