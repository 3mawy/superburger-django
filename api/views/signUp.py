from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from api.models import Address, Customer
from api.serializers import UserSerializer


# @api_view(['POST'])
# @permission_classes((permissions.IsAuthenticated,))
# def sign_up(request):
#     return
#

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer
