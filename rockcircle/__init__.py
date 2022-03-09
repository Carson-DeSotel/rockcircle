from flask import Flask

# needs to be initialized before importing views
app = Flask(__name__)

# establish config from config file
from config import Config
app.config.from_object(Config)

# import after creating app
from rockcircle import views, db

# initialize the database
db.init_db()