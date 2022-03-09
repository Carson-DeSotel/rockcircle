import os

from rockcircle import app

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret!'
  DATABASE = os.path.join(app.instance_path, 'rockcircle.sqlite')