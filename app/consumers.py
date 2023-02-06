import json

from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    def receive(self,text_data=None,bytes_data=None):
        obj=json.loads(text_data)
        print("received: ",obj)

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"],
        })
        self.send(json_string)
    #웹소켓 수신 메세지 처리 위해 receive 메서드 재정의
    #새로운 text/bytes frame 받을 때마다 호출