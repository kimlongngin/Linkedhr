from channels.routing import route
from chat import consumers

channel_routing = [
	route('websocket.connect', consumers.ws_add, path=r'^/chat/$') ,
	route('websocket.receive', consumers.ws_message, path=r'^/chat/$') ,
	route('websocket.disconnect', consumers.ws_disconnect, path=r'^/chat/$'),
	#route("websocket.connect", consumers.ws_connect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    #route("websocket.receive", consumers.ws_message, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    #route("websocket.disconnect", consumers.ws_disconnect, path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]
