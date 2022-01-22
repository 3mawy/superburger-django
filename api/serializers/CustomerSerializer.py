from rest_framework import serializers

from api.models import Customer, Area, Address, Cart
from api.serializers import CartSerializer


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        depth = 1
        fields = ('id', 'address', 'area')


class CustomerSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, required=False)
    # cart = serializers.ModelSerializer(required=False)

    class Meta:
        model = Customer
        fields = '__all__'

