from rest_framework import serializers
from api.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        depth = 1
        fields = ('id', 'name', 'description', 'price',
                  'active', 'menu_items')
