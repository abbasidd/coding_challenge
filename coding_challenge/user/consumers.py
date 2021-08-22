from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import User,Deposits
import json
from user.api.serializers import Deposits_serializer
import random
from django.core.cache import caches
#websocket implementation 
class Deposit(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deposits = None
        self.user = None
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['user_id']
        self.user = User.objects.get(id = self.room_name)
        if caches.all()[0].get(self.user.username):
            self.deposits = caches.all()[0].get('usman')
        else:
            ser1 = Deposits_serializer(Deposits.objects.filter(user = self.user), many=True)
            self.deposits = ser1.data
            caches.all()[0].set(self.user.username,self.deposits)
        
        self.room_group_name = self.user.username

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept() 

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['action'] =='buy' :
            text_data_json['user_id']=self.user.id
            async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'deposit',
                 'amount' : text_data_json['amount'] ,
                  'currency' : text_data_json['currency'],
                'user_id':self.user.id,
            }
        )
        elif text_data_json['action'] == 'get':
            async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'get',
            }
        )

            

    def deposit(self, event):
        ser = Deposits_serializer(data = event,partial=True)
        if ser.is_valid():
            ser.save()
            self.send({'deposit':ser.data})
        else:
            print(ser.errors)
        

    def get(self, event):
        for item in self.deposits:
            item['amount']  = item['amount']+random.randint(0,9)
            item['user_id']= self.user.id
        caches.all()[0].set(self.user.username,self.deposits)
        self.send(text_data=json.dumps({'deposits':self.deposits}))
    def disconnect(self, close_code):
        d_serilizer = Deposits_serializer(data = self.deposits , many=True )
        if d_serilizer.is_valid():
            d_serilizer.save()
        else:
            print(d_serilizer.errors)

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )