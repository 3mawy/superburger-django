from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import UserSerializer, GroupSerializer

from api import serializers
from api import models
from api.models import PlacedOrder


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

    def get_queryset(self):

        user = self.request.user
        return PlacedOrder.objects.filter(customer__user=user)


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