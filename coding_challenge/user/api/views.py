from django.db.models.query import QuerySet
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from rest_framework import viewsets,status
from .serializers import User_RegistrationSerializer,Deposit_serializer,Deposits_serializer
from user.models import Deposits, User
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = User_RegistrationSerializer
    queryset = User.objects.all()
class Deposits_view(APIView):
    def post(self , request ):
        print(request.data)
        serializer = Deposits_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    def get(self , request ,id=None):
        if id == None:
            querySet = Deposits.objects.all()
            serializer = Deposits_serializer(querySet , many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else : 
            instance = Deposits.objects.filter(user__id = id)
            serializer = Deposits_serializer(instance , many =True)
            return Response(serializer.data, status=status.HTTP_200_OK)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = User_RegistrationSerializer
#     queryset = User.objects.all()
    