from flask_socketio import send, emit

from rockcircle import app, socketio

@socketio.on('connect')
def test_connect(auth):
  print('Client connected')
  emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
  print('Client disconnected')

@socketio.event
def connect():
  emit('my_response', {'data': 'Connected'})