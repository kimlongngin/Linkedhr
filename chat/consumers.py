from channels import Channel, Group
from channels.sessions import channel_session, enforce_ordering
from .models import Room, Message, RoomUser
from channels.auth import channel_session_user, channel_session_user_from_http
from django.contrib.auth.views import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import json

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
	#user_id = data["userid"]
	#label = 'chat-'+str(user_id)+'-'+str(sup_user)
	#room = Room.objects.get(label=label)
	
	# Add pair of user and admin to array.
	#arrusrs = [user_id, sup_user]
	#if room:
		#Message.objects.create(room=room, message=data["usermsg"])
		#Group('chat').send({'text':message.content['text']})
	#else:
		#new_room = Room.objects.create(name="TextField"+ label, label=label)
		#Message.objects.create(room=new_room, message=data["usermsg"])
		#Group('chat').send({'text':message.content['text']})
	
	Group('chat').send({'text':message.content['text']})
#disconnect
@channel_session
def ws_disconnect(message):
	Group('chat').discard(message.reply_channel)
	#Group("chat-%s" % message.user.username).discard(message.reply_channel)
