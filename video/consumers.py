from channels.generic.websocket import AsyncJsonWebsocketConsumer

class VideoChat(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def recieve_json(self,content):
         pass