from rest_framework import serializers
from user.models import User,Deposits
from django.db import transaction


class User_RegistrationSerializer(serializers.ModelSerializer):   
    password = serializers.CharField(
        write_only=True,) 
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
class Deposits_serializer(serializers.ModelSerializer):
    # deposits_wallet = Deposit_serializer(read_only=True)
    # deposit_id = serializers.PrimaryKeyRelatedField(queryset=Deposits.objects.all(), write_only=True )
    user = User_RegistrationSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True )

    class Meta:
        model = Deposits 
        fields = ['id','amount','currency','user','user_id']
    def create(self, validated_data):
        user = validated_data.pop('user_id')
        try:
            #for the sake of simplcity i just update if deposit instance exists
            obj = Deposits.objects.get(user=user, currency =validated_data['currency'])
            obj.amount = validated_data['amount']
            obj.save()
            return obj
        except:

            instance = Deposits.objects.create(user=user,**validated_data)
            return instance