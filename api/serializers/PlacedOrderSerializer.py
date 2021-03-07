from rest_framework import serializers
from api.models import PlacedOrder
from api.serializers import OrderItemSerializer


class PlacedOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = PlacedOrder
        fields = ('id', 'order_time', 'delivery', 'delivery_notes', 'total_price',
                  'complete', 'delivery_address', 'customer', 'order_items', 'status')



