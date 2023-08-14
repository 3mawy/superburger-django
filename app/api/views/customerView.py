from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView

from api import models
from api import serializers
from api.models import Customer


class CurrentCustomerView(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all().order_by('id')
    serializer_class = serializers.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        return Customer.objects.filter(user=user)


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
