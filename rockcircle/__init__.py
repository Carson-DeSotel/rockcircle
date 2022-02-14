from flask import Flask
from flask_socketio import SocketIO

from config import Config

### needs to be initialized before importing views
async_mode = None
app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app, async_mode=async_mode)

from rockcircle import views, handles

if __name__ == '__main__':
    sio.run(app)