from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'title', 'completed')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'description')


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Size
        fields = ('id', 'name')


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ('id', 'name', 'description')


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Offer
        fields = ('id', 'name', 'description')


