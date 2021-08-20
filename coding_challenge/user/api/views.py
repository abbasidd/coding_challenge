from rest_framework import viewsets
from .serializers import User_RegistrationSerializer
from user.models import User
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = User_RegistrationSerializer
    queryset = User.objects.all()

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = User_RegistrationSerializer
#     queryset = User.objects.all()
    