from rest_framework import serializers
from api.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    item_price = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
    total_price = serializers.DecimalField(max_digits=8, decimal_places=2, required=False)

    class Meta:
        model = OrderItem
        fields = '__all__'

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)
