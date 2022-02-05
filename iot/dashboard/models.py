from django.db import models

# Create your models here.

class Data(models.Model):
    floor = models.CharField(max_length=64)
    room = models.IntegerField()
    product = models.CharField(max_length=64)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.floor} {self.room} {self.product} {self.status}"

