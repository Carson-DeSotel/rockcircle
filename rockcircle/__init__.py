from flask import Flask

# needs to be initialized before importing views
app = Flask(__name__)

# establish config from config file
from config import Config
app.config.from_object(Config)

# import after creating app
from rockcircle import views, db, game

# initialize the database each time the app is ran
db.init_db()