from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer

from . import serializers
from . import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.

# @api_view(['GET', 'POST'])
# def api_overview(request):
#     return Response("API BASE POINT", safe=False)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all().order_by('id')
    serializer_class = serializers.TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('id')
    serializer_class = serializers.CategorySerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = models.Size.objects.all().order_by('id')
    serializer_class = serializers.SizeSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = models.MenuItem.objects.all().order_by('id')
    serializer_class = serializers.MenuItemSerializer
    filterset_fields = ['category']


class OfferViewSet(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all().order_by('id')
    serializer_class = serializers.OfferSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all().order_by('id')
    serializer_class = serializers.OrderItemSerializer


class PlacedOrderViewSet(viewsets.ModelViewSet):
    queryset = models.PlacedOrder.objects.all().order_by('id')
    serializer_class = serializers.PlacedOrderSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all().order_by('id')
    serializer_class = serializers.StatusSerializer

