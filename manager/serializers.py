from .models import CustomUser, vehicle, transactions, pumpInfo
from rest_framework import serializers


class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = ('vehicleNumber', 'quantity')


class TankdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'


class PumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = pumpInfo
        fields = '__all__'
