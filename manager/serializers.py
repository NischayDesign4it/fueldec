from .models import CustomUser, vehicle
from rest_framework import serializers



class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = ('vehicleNumber', 'quantity')


class TankdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'