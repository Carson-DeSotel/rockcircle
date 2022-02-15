from flask_socketio import send, emit

from rockcircle import app, socketio, thread, thread_lock
from rockcircle.timer import Timer

@socketio.on('connect')
def test_connect(auth):
  print('Client connected')
  emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
  print('Client disconnected')

@socketio.event
def connect():
  global timer 
  timer = Timer(socketio)
  emit('my_response', {'data': 'Connected'})

  print('starting background task...')
  socketio.start_background_task(target=timer.run)

@socketio.event
def handle_login(data):
  print('handling login...', data['data'])

@socketio.event
def handle_timer_start():
  print('starting timer...')
  timer.start()

@socketio.event
def handle_timer_stop():
  print('stopping timer...')
  timer.pause()

