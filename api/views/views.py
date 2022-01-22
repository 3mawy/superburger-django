from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer

from api import serializers
from api import models
from api.models import PlacedOrder


# Create your views here.

# @api_view(['GET', 'POST'])
# def api_overview(request):
#     return Response("API BASE POINT", safe=False)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('id')
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


class SizeViewSet(viewsets.ModelViewSet):
    queryset = models.Size.objects.all().order_by('id')
    serializer_class = serializers.SizeSerializer
    permission_classes = [permissions.AllowAny]


class CarouselImageViewSet(viewsets.ModelViewSet):
    queryset = models.CarouselImage.objects.all().order_by('id')
    serializer_class = serializers.CarouselImageSerializer
    permission_classes = [permissions.AllowAny]


class MenuItemSizeViewSet(viewsets.ModelViewSet):
    queryset = models.MenuItemSize.objects.all().order_by('id')
    serializer_class = serializers.MenuItemSizeSerializer
    permission_classes = [permissions.AllowAny]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = models.MenuItem.objects.all().order_by('id')
    serializer_class = serializers.MenuItemSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    ordering_fields = ('sizes__size__price', 'score')
    permission_classes = [permissions.AllowAny]


class OfferViewSet(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all().order_by('id')
    serializer_class = serializers.OfferSerializer
    permission_classes = [permissions.AllowAny]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all().order_by('id')
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.AllowAny]


class PlacedOrderViewSet(viewsets.ModelViewSet):
    queryset = models.PlacedOrder.objects.all().order_by('id')
    serializer_class = serializers.PlacedOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlacedOrder.objects.filter(customer__user=user)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all().order_by('id')
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.AllowAny]


class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all().order_by('id')
    serializer_class = serializers.AreaSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all().order_by('id')
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all().order_by('id')
    serializer_class = serializers.ImageSerializer
    permission_classes = [permissions.AllowAny]


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = models.Extra.objects.all().order_by('id')
    serializer_class = serializers.ExtraSerializer
    permission_classes = [permissions.AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all().order_by('id')
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.AllowAny]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all().order_by('id')
    serializer_class = serializers.CartItemSerializer
    permission_classes = [permissions.AllowAny]
