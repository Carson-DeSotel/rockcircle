import os

from rockcircle import app

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret!'