from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api import models
from api.models import PlacedOrder, Status, Customer, OrderItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'addresses']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class MenuItemSizeSerializer(serializers.ModelSerializer):
    size = serializers.CharField(source='size.name')
    menu_item = serializers.IntegerField(source='menu_item.id')

    class Meta:
        model = models.MenuItemSize
        fields = ('menu_item', 'size', 'price')


class SizeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = models.Size
        fields = ('id', 'name')


class MenuItemSerializer(serializers.ModelSerializer):
    sizes = MenuItemSizeSerializer(source='menu_item', many=True)

    class Meta:
        model = models.MenuItem
        depth = 1
        fields = ('id', 'name', 'description', 'ingredients',
                  'active', 'score', 'category', 'sizes')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        depth = 1
        fields = ('id', 'name', 'description', 'price',
                  'active', 'menu_items')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class PlacedOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = PlacedOrder
        fields = ('id', 'order_time', 'delivery', 'delivery_notes', 'total_price',
                  'complete', 'delivery_address', 'customer', 'order_items', 'status')

    def create(self, validated_data):
        print(validated_data)
        order = PlacedOrder.objects.create(**validated_data)
        order.order_items.set(validated_data['order_items'])
        # new_list = validated_data.
        return order


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'
