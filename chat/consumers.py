from channels import Channel, Group
from channels.sessions import channel_session, enforce_ordering
from .models import Room, Message, RoomUser
from channels.auth import channel_session_user, channel_session_user_from_http
from django.contrib.auth.views import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import json
from chat.views import home, chat, ichat

# Connect
@channel_session
def ws_add(message):
	message.reply_channel.send({"accept":True})
	Group('chat').add(message.reply_channel)
	#Group("chat-%s" % message.user.username).add(message.reply_channel)

# Receive
@channel_session
def ws_message(message, *args, **kwargs):
	#label = message.channel_session['room']
	#superuser = User.objects.filter(is_superuser=True)
	#arrsup_user = []
	#for i in superuser:
		#arrsup_user= [i.id]
	#sup_user= arrsup_user[0]
	
	data = json.loads(message['text'])
	room_id = data["room_id"]
	user_id = data["userid"]
	
	try:		
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		raise Http404("Error user connection.")

	try:
		room = Room.objects.get(label=room_id)
		Message.objects.create(user = user, room=room, message=data["usermsg"])
		Group('chat').send({'text':message.content['text']})
	except Room.DoesNotExist:
		new_room = Room.objects.create(name="TextField"+ room_id, label=room_id)
		Message.objects.create(user = user, room=new_room, message=data["usermsg"])
		Group('chat').send({'text':message.content['text']})
	
	#Group('chat').send({'text':message.content['text']})
#disconnect
@channel_session
def ws_disconnect(message):
	Group('chat').discard(message.reply_channel)
	#Group("chat-%s" % message.user.username).discard(message.reply_channel)
