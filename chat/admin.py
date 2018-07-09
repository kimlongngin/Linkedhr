# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Room, Message, RoomUser
# admin.site.site_header='Linkedhr administration'

admin.site.register(Room)
admin.site.register(RoomUser)
admin.site.register(Message)
