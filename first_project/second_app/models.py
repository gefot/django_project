# python manage.py migrate
# python manage.py makemigrations

from django.db import models


class Device(models.Model):
    mac_address = models.CharField(max_length=12, unique=True)
    extension = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    timestamp = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.mac_address, self.extension)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return "{} - {} - {}".format(self.first_name, self.last_name, self.email)
