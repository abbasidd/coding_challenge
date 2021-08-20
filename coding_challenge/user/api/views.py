from rest_framework.response import Response 
from rest_framework.decorators import APIView
from rest_framework import viewsets,status
from .serializers import User_RegistrationSerializer,Deposit_serializer,Deposits_serializer
from user.models import User
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = User_RegistrationSerializer
    queryset = User.objects.all()
class Deposits_view(APIView):
    def post(self , request , *args, **kwargs):
        serializer = Deposits_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = User_RegistrationSerializer
#     queryset = User.objects.all()
    