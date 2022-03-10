from flask import Flask
import logging
from logging.config import fileConfig 

# needs to be initialized before importing views
app = Flask(__name__)

# establish config from config file
from config import Config
app.config.from_object(Config)

# establish logging config
fileConfig('logging_config.ini')
logger = logging.getLogger()

# import after creating app
from rockcircle import views, db, game

# initialize the database each time the app is ran
db.init_db()