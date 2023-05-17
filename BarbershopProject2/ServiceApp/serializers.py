from rest_framework import serializers
from ServiceApp.models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('id', 'barber_name', 'client_name', 'price')
