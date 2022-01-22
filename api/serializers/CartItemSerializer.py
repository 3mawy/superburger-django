from rest_framework import serializers
from api.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        depth = 1
        fields = '__all__'
