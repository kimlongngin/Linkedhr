from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from .models import Room, RoomUser, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    title = "my chat room"
    room = {}
    if request.user.is_authenticated():			
    	if request.user.is_superuser == True:
    		room = getallroomchat()
    		return render(request, 'index.html', {"title":title, 'room':room})
    	else:
    		return render(request, 'index.html', {"title":title})
    else:
		return redirect('linkedhr:login')

# tracking message and rooms 
def trackingMessageRoom(chk_user, user_name, pk):
	# use try--except here for instead of if else statement to detect error when 
	# no data retrieving from room models and create a new room  in exception 
	message = {}
	try:
		# filter data from message which by room label clause 
		room = Room.objects.get(label=pk)
		message = reversed(room.messages.filter().order_by('-timestamp')[:10])
		# context data will use at ichat.html
	except Room.DoesNotExist:
		# create new room when room is empty
		if chk_user == True:
			message = message
		else:
			message = {}
			new_room_create = Room.objects.create(name = user_name, label = pk)
	return message

# get all room for admin.
def getallroomchat():
	room = Room.objects.filter(is_status = True)
	return room

# We are taking the id of user to be a chat-room. 
# First, This chat can use with admin
# Second, This chat can use with the recruitor with seeker  
def ichat(request, pk):
	template = loader.get_template('ichat.html')
	context = {}
	room = {}
	if request.user.is_authenticated():			
		# label is get from the url name with pk parameter.
		room_label = pk
		user_name = request.user.username
		# Start to check data from form with post condition
		if request.method !="POST":
			# Call functions function for checking message and room
			if request.user.is_superuser == True:
				chk_user=True
				message = trackingMessageRoom(chk_user, user_name, room_label)
			else:
				# Protect from other user use owner chat.
				if str(request.user.id) == str(room_label):
					chk_user=False
					message = trackingMessageRoom(chk_user, user_name, room_label)
				else:
					raise Http404("No room chat.")
			# return HttpResponseRedirect(reverse('chatroom'))
			context = {'messages1': message}
			return HttpResponse(template.render(context,request))
		else:

			# Call functions function for checking message and room			
			if request.user.is_superuser == True:
				chk_user=True
				message = trackingMessageRoom(chk_user, user_name, room_label)
			else:
				# Protect from other user use owner chat.
				if str(request.user.id) == str(room_label):
					chk_user=False
					message = trackingMessageRoom(chk_user, user_name, room_label)
				else:
					raise Http404("No room chat.")

			user_id = request.user.id
			username = request.user.username

			#return render(request, 'ichat.html', {'messages1': messages, "username":username, "userid":user_id})
			return render(request, 'chat.html', {'messages1': message, "title":"Title", "username":username, "userid":user_id})
	else:
		return redirect('linkedhr:login')


def chat(request, *args, **kwargs):
	# Retrieve super user for mix with user to crate room
	#title = "Chat"
	template = loader.get_template('chat.html')
	context = {}
	#superuser = User.objects.filter(is_superuser=True)
	#arrsup_user = []
	#for i in superuser:
		#arrsup_user= [i.id]
	# Create room name by combining login user with a "superuser"	
	#label = 'chat-'+str(request.user.id)+'-'+str(arrsup_user[0])
	
	#room = Room.objects.get(label=label)
	#messages = reversed(room.messages.filter().order_by('-timestamp')[:10])
	
	if request.user.is_authenticated():			
	    if request.method !="POST":
	        #context ={ 'messages1':messages }
	        return HttpResponseRedirect(reverse('chatroom'))
	    	#return HttpResponse(template.render(context,request))
	    else:
	    	user_id = request.user.id
	    	username = request.user.username
	    	
	    	return render(request, 'chat.html', {"username":username, "userid":user_id})
	    	#return render(request, 'chat.html', {'messages1': messages, "title":title, "username":username, "userid":user_id})
	else:
		return redirect('linkedhr:login')	      
	
def new_room(request):
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
	return redirect(chat_room, label=label)
