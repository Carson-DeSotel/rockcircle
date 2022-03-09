$(document).ready(function() { 
  var socket = io();
  socket.on('connect', function() {
      socket.emit('my event', {data: 'I\'m connected!'});
  });

  $('form#login').submit(function(event) {
      socket.emit('handle_login', {name: $('#fname').val()});
      return false;
  });

  socket.on('update_players', function(msg) {
    for(p_name in msg['data']['names']) {
      console.log(p_name)
      $('#players').append('<p>' + p_name + '</p>').html();
    }
    
  });
});