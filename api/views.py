from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, authentication
from rest_framework import permissions
from rest_framework.views import APIView

from api.serializers import UserSerializer, GroupSerializer, MenuItemSerializer, PlacedOrderSerializer

from . import serializers
from . import models
from .models import Size, PlacedOrder, Address, Customer, Status, OrderItem, MenuItem, MenuItemSize, Offer


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

json_test = {
    "placed_order": {
        "order_time": "04:14:49.289732",
        "delivery": True,
        "delivery_notes": "ggg",
        "complete": False,
        "delivery_address": 1,
        "customer": 1,
        "order_items": [],
        "status": 1
    },
    "order_items": [{
        "quantity": 2,
        "size": 3,
        "comments": "aa",
        "placed_order": 1,
        "offer": None,
        "item": 1
    }]
}


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def post_order(request):
    grand_total = 0

    placed_order = json_test.get('placed_order')
    order_time = placed_order.get('order_time')
    delivery = placed_order.get('delivery')
    delivery_notes = placed_order.get('delivery_notes')
    complete = placed_order.get('complete')
    delivery_address = Address.objects.get(pk=placed_order.get('delivery_address'))
    customer = Customer.objects.get(pk=placed_order.get('customer'))
    status = Status.objects.get(pk=placed_order.get('status'))

    order = PlacedOrder.objects.create(order_time=order_time, delivery=delivery, delivery_notes=delivery_notes,
                                       complete=complete, total_price=0, delivery_address=delivery_address,
                                       customer=customer, status=status)

    order_items = json_test.get('order_items')
    for order_item in order_items:
        quantity = order_item.get('quantity')
        size = order_item.get('size')
        comments = order_item.get('comments')
        placed_order = order
        if order_item.get('item'):
            item = MenuItem.objects.get(pk=order_item.get('item'))
            offer = None
            item_size = MenuItemSize.objects.get(menu_item=item, size=size)
            price = item_size.price
        else:
            offer = Offer.objects.get(pk=order_item.get('offer'))
            item = None
            price = offer.price

        total_price = price * quantity
        OrderItem.objects.create(quantity=quantity, item_price=price, total_price=total_price,
                                 comments=comments, placed_order=placed_order,
                                 item=item, offer=offer)
        grand_total = grand_total + total_price
    order.total_price = grand_total
    order.save()
    return Response({"message": "order and order items added Successfully!", "data": "a"})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('id')
    serializer_class = serializers.CategorySerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = models.Size.objects.all().order_by('id')
    serializer_class = serializers.SizeSerializer


class MenuItemSizeViewSet(viewsets.ModelViewSet):
    queryset = models.MenuItemSize.objects.all().order_by('id')
    serializer_class = serializers.MenuItemSizeSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = models.MenuItem.objects.all().order_by('id')
    serializer_class = serializers.MenuItemSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['category']
    ordering_fields = ('sizes', 'score')


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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all().order_by('id')
    serializer_class = serializers.CustomerSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = models.Area.objects.all().order_by('id')
    serializer_class = serializers.AreaSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all().order_by('id')
    serializer_class = serializers.AddressSerializer
