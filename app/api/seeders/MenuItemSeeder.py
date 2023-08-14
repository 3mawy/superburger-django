from rest_framework import serializers
from api.models import MenuItem, Size, MenuItemSize


class SizeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Size
        fields = ('id', 'name')


class MenuItemSizeSerializer(serializers.ModelSerializer):
    size = serializers.CharField(source='size.name')
    menu_item = serializers.IntegerField(source='menu_item.id')

    class Meta:
        model = MenuItemSize
        fields = ('menu_item', 'size', 'price')


class MenuItemSerializer(serializers.ModelSerializer):
    sizes = MenuItemSizeSerializer(source='menu_item', many=True)

    class Meta:
        model = MenuItem
        depth = 1
        fields = ('id', 'name', 'description', 'ingredients',
                  'active', 'score', 'category', 'sizes')
