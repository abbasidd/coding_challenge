from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/deposit/(?P<user_id>\w+)/$',
            consumers.Deposit.as_asgi()),
]
