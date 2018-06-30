
$(document).ready(function(){
	var socket = new WebSocket('ws://127.0.0.1:8000/chat/');
	socket.onopen = websocket_welcome;
	socket.onmessage = websocket_message_show;

	$('#Chatform').submit(function(event){
		event.preventDefault();
		var message_data={
			'username':$('input[name="username"]').val(),
			'usermsg':$('input[name="usermsg"]').val(),
		}
		socket.send(JSON.stringify(message_data));
		$('#Chatform')[0].reset();

		/* coding = "<h5>" + message_data.username + "</h5>" +
			"<p class = 'coding'>"+ message_data.usermsg + "</p>";
		$('#messageCanvas').append(coding); */
		
    });


});

function websocket_welcome(){}


function websocket_message_show(e) {
	if (typeof e !== 'undefined') {
	    var message_data = JSON.parse(e.data);
	    coding = "<h5>" + message_data.username + "</h5>" +
			"<p class = 'coding'>"+ message_data.usermsg + "</p>";
		$('#messageCanvas').append(coding);
	}
}
