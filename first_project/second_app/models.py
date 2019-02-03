# python manage.py migrate
# python manage.py makemigrations

from django.db import models
from datetime import datetime


# Create your models here.
class DN(models.Model):
    extension = models.CharField(max_length=20, unique=True)
    callername = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.extension, self.callername)


class Device(models.Model):
    mac_address = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=30)
    dn = models.ForeignKey(DN)
    registration_status = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "{} - {}".format(self.mac_address, self.dn)
