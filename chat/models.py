# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    is_status = models.BooleanField(default=True)

class Message(models.Model):
	user =  models.ForeignKey(User, related_name='user_sms', on_delete=models.CASCADE)
	room = models.ForeignKey(Room, related_name='messages')
	handle = models.TextField()
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_status = models.BooleanField(default=True)
IS_TYPE = (
    ('1', 'user-admin'),
    ('2', 'seeker-recruitor'),
    ('3', 'recruitor-seeker'),
)

class MessageType(models.Model):
	message = models.ForeignKey(Message, related_name='message_message_type', on_delete=models.CASCADE)
	ms_type = models.CharField(max_length=20, choices=IS_TYPE)	

class RoomUser(models.Model):
	room = models.ForeignKey(Room, related_name='room_user')
	user =  models.ForeignKey(User, related_name='room_user_user', on_delete=models.CASCADE)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)