from django.urls import path
from app.consumers import EchoConsumer

# 장고랑 다른 점:
# 장고에서 찾아서 읽어가는 것이 아니고
# asgi.py 직접 임포트하여 지정 -> 이름 달라도 상관 없음

websocket_urlpatterns = [
 path("ws/echo/", EchoConsumer.as_asgi()),
]
