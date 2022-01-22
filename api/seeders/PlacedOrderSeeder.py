from rest_framework import serializers
from api.models import PlacedOrder
from api.serializers import OrderItemSerializer, StatusSerializer, CustomerSerializer


class PlacedOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = PlacedOrder
        fields = ('id', 'delivery', 'delivery_notes',
                  'total_price', 'delivery_address',
                  'customer', 'order_items', 'status')

    def create(self, validated_data):
        return PlacedOrder.objects.create(**validated_data)
