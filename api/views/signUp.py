# @api_view(['POST'])
# @permission_classes((permissions.IsAuthenticated,))
# def sign_up(request):
#     return
#
from django.db import transaction
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import Cart, Address, Area
from api.serializers import UserSerializer, CustomerSerializer


@api_view(['POST'])
@transaction.atomic
@permission_classes((permissions.AllowAny,))
def signup(request):
    info = request.data
    with transaction.atomic():
        basic_info = {
            "username": info.get('username'),
            "password": info.get('password'),
            "first_name": info.get('full_name'),
            "email": info.get('email'),
        }

        serializer = UserSerializer(data=basic_info)
        serializer.is_valid(True)
        user = serializer.save()
        user.set_password(basic_info['password'])
        cart = Cart.objects.create()

        detailed_info = {
            "full_name": info.get('full_name'),
            "mobile_number": info.get('mobile_number'),
            "user": user.id,
            "cart": cart.id,
            "email": info.get('email'),

        }

        customerSerializer = CustomerSerializer(data=detailed_info)
        customerSerializer.is_valid(True)
        customer = customerSerializer.save()
        area = Area.objects.get(id=1)
        address = Address.objects.create(area=area, address=info.get('address'), customer=customer)
        customer.addresses.set([address])
        customer.save()
        user.save()
        cart.save()

        return Response({"message": "Signed up Successfully!",
                         "customer_email": user.email})
