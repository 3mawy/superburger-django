from rest_framework import serializers
from api.models import  Cart

from api.serializers.CartItemSerializer import CartItemSerializer
from api.serializers import OrderItemSerializer


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, required=False)

    class Meta:
        model = Cart
        depth = 1
        fields = ('id', 'total_price', 'cart_items')

