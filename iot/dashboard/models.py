from django.db import models

# Create your models here.

class Data(models.Model):
    floor = models.CharField(max_length=64)
    room = models.CharField(max_length=3)
    product = models.CharField(max_length=64)
    status = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.floor} {self.room} {self.product} {self.status}"

