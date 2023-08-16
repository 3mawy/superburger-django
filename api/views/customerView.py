from rest_framework import viewsets

from api import models
from api import serializers
from api.models import Customer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def current_customer(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.get(user=user)
        serialized_customer = serializers.CustomerSerializer(customer)

        return Response({
            "message": "Authenticated user's information",
            "user": serialized_customer.data
        })
    else:
        return Response({
            "message": "Unauthenticated user",
        })
@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def current_customer_orders(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.get(user=user)
        orders = customer.placedOrders.all()
        serialized_orders = serializers.PlacedOrderSerializer(orders, many=True)
        return Response({
            "orders": serialized_orders.data
        })
    else:
        return Response({
            "message": "Unauthenticated user",
        })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all().order_by('id')
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

#
# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticated,))
# def get_customer(request):
#     user = request.user
#     print(user)
#
#     customer = Customer.objects.filter(user=user)
#     print(customer)
#     customer_serializer = serializers.CustomerSerializer('json', [customer, ])
#     customer_serializer.is_valid()
#     return Response(customer_serializer.data)
#
#
