from django.db import models


class ServiceModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    barber_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    price = models.IntegerField()
    objects = models.Manager()
