from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db

@app.route('/', methods=['GET', 'POST'])
def index():
  if 'to_roles' in request.form:
    # get role data from database
    rows = query_db('SELECT * FROM Roles')
    # render role data in roles.html
    return render_template('roles.html', rows = rows)

  elif 'to_index' in request.form:
    return render_template('index.html')
  
  return render_template('index.html', title='Home')

@app.teardown_appcontext
def close_connection(exception):
  """
  close down the database as the app is being closed
  """
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()