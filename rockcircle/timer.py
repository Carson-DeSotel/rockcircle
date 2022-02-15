from rockcircle import socketio

class Timer(object):
  is_active = False 
  seconds   = 0

  def __init__(self, socketio):
    self.socketio = socketio

  def run(self):
    print('running...')
    while True:
      self.seconds += 1
      self.socketio.emit('timer_response',
                        {'data': 'Timer', 'seconds': self.seconds})
      self.socketio.sleep(1)

  def start(self):
    self.is_active = True

  def pause(self):
    self.is_active = False 

  def reset(self):
    self.seconds = 0
