from .models import CustomUser, vehicle, transactions
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
        fields = ('vehicleNumber', 'dispensedQuantity')