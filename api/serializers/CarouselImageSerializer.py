from rest_framework import serializers
from api.models import Category, CarouselImage


class CarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        depth = 1
        fields = '__all__'
