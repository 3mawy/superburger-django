from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import Customer, Cart


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=get_user_model().objects.all())])

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    # def create(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     user.set_password(validated_data['password'])
    #     cart = Cart.objects.create()
    #     customer = Customer.objects.create(full_name=validated_data['first_name'],
    #
    #                                        user=user, cart=cart)
    #     customer.save()
    #     user.save()

        # return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
