from rest_framework import serializers
from user.models import User,Wallet,Deposits
from django.db import transaction


class User_RegistrationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['email', 'password', 'username',
                  'first_name', 'last_name', ]
       
    @transaction.atomic
    def create(self, validated_data):
        try:
            User.objects.get(email=validated_data['email'])
            return 'error'
        except:
            password = validated_data['password']
            account = User.objects.create(
                    email=validated_data['email'],
                    username= validated_data['username'],
                    first_name= validated_data['first_name'],
                    last_name= validated_data['last_name'],
            )
            account.set_password(password)
            account.save()
            return account

class Deposit_serializer(serializers.ModelSerializer):
    class  Meta:
        model = Deposits
        fields  = '__all__'
class Wallet_serializer(serializers.ModelSerializer):
    Deposits = Deposit_serializer()
    class Meta:
        model = Wallet 
        fields = ['']