from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db
from rockcircle.game import add_player

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if request.form['add_player']:
      pname = request.form.get('pname')
      prole = request.form.get('prole')
      add_player(pname, prole)
  return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
  if 'to_roles' in request.form:
    # get role data from database
    rows = query_db('SELECT * FROM Roles')
    print(rows)
    # render role data in roles.html
    return render_template('roles.html', rows = rows)

  elif 'to_admin' in request.form:
    return render_template('admin.html')
  return render_template('admin.html')

@app.teardown_appcontext
def close_connection(exception):
  """
  close down the database as the app is being closed
  """
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()