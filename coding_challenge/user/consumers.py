from channels.generic.websocket import WebsocketConsumer

class Online(WebsocketConsumer):
    def connect(self):
        self.accept()
