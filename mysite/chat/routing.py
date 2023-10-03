# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # instantiate consumer with ASGI
    re_path(r"ws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
