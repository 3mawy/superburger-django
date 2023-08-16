from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from api.models import Customer
from api.serializers import UserSerializer, GroupSerializer, CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (permissions.AllowAny,)

        return super(UserViewSet, self).get_permissions()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class CurrentUserView(viewsets.ModelViewSet):
#     queryset = Customer.objects.all().order_by('id')
#     serializer_class = CustomerSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         user = self.request.user
#         return User.objects.filter(id=user.id)
