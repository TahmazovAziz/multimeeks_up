import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ComentName,Message,Niknaim
class ChatRoom(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.groups_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.groups_name , self.channel_name)
        await self.accept()

    async def disconnect(self , code):
        await self.channel_layer.group_discard(self.groups_name,self.channel_name)

    async def receive(self , text_data):
        text_data_json = json.loads(text_data)
        niknaim_content = text_data_json['niknaim']
        message_content = text_data_json['message']
        chat_record = await sync_to_async(ComentName.objects.filter(room_name=self.groups_name).first)()
        if chat_record is not None:
            chat_name = chat_record
        else:
            chat_name = await sync_to_async(ComentName.objects.create)(room_name=self.groups_name)
        niknaim = await sync_to_async(Niknaim.objects.create)(name=niknaim_content)
        print('pr1')
        message = await sync_to_async(Message.objects.create)(message_text=message_content,niknaimid=niknaim,chatid=chat_name)
        print('pr2')

        context = {"type":"chat.message", "niknaim":niknaim_content , "message":message_content}
        print('pr3')

        await self.channel_layer.group_send(self.groups_name , context)
        print('pr4')
        
    async def chat_message(self,event):
        message = event["message"]
        niknaim = event["niknaim"]
        await self.send(text_data=json.dumps({"message":message , "niknaim":niknaim}))