from rest_framework import serializers
from .models import Customers

class customerSerializar(serializers.ModelSerializer):

    class Meta:
        model= Customers
        fields=('first_name','last_name','email','message')


