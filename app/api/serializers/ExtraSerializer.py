from rest_framework import serializers
from rest_framework.response import Response

from api.models import Extra


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = '__all__'

