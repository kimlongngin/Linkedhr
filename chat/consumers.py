from channels import Group

# Connect
def ws_add(message):
	message.reply_channel.send({"accept":True})
	Group('chat').add(message.reply_channel)

# Receive
def ws_message(message):
	Group('chat').send({'text':message.content['text']})

#disconnect
def ws_disconnect(message):
	Group('chat').discard(message.reply_channel)
