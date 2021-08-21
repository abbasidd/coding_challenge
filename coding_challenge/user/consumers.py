from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import User,Deposits
import json
from user.api.serializers import Deposits_serializer
import random

class Deposit(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deposits = None
        self.user = None
    def connect(self):
        print(self)
        self.room_name = self.scope['url_route']['kwargs']['user_id']
        self.user = User.objects.get(id = self.room_name)
        ser1 = Deposits_serializer(Deposits.objects.filter(user = self.user), many=True)
        self.deposits = ser1.data
        print(self.deposits)
    
        print(self.user)
        self.room_group_name = self.user.username

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # action = text_data_json.pop('action')
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
        print('kkkkkkk')
        print(self.deposits)
        for item in self.deposits:
            # print('item')
            # print(random.randint(0,9))round(random.uniform(10.5, 75.5),4)
            item['amount']  = item['amount']+random.randint(0,9)
            item['user_id']= self.user.id
        self.send(text_data=json.dumps({'deposits':self.deposits}))
        print(self.deposits)
    def disconnect(self, close_code):
        d_serilizer = Deposits_serializer(data = self.deposits , many=True )
        if d_serilizer.is_valid():
            d_serilizer.save()
        else:
            print(d_serilizer.errors)
        # Workflow.objects.update_or_create(obj = self.workflow, user = User.objects.get(id = self.workflow['user_id'])  ,name = self.room_name7)

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )