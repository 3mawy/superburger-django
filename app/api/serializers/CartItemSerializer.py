from rest_framework import serializers
from api.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        depth = 1
        fields = ('id', 'quantity', 'item_price', 'total_price', 'comments', 'extras_price', 'size', 'offer', 'item', 'extras' )
