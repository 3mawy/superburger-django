from rest_framework import serializers
from api.models import  Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        depth = 1
        fields = '__all__'

