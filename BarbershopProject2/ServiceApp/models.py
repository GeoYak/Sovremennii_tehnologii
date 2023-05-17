from django.db import models


# Create your models here.

class ServiceModel(models.Model):
    id = models.AutoField(primary_key=True)
    barber_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    price = models.IntegerField()
