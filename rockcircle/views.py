from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db
from rockcircle.game import add_player, drop_player

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if request.form['action'] == 'Add Player':
      pname = request.form.get('pname').upper()
      prole = request.form.get('prole').upper()
      add_player(pname, prole)

    elif request.form['action'] == 'To Vote':
      rows = query_db('SELECT pname FROM Roles')
      return render_template('vote.html', rows = rows)
      
    elif request.form['action'] == 'Cast Vote':
      pname = request.form['name']
      print('VOTED OFF:', pname)
      drop_player(pname)

  return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
  if request.form['action'] == 'To Roles':
    # get role data from database
    rows = query_db('SELECT * FROM Roles')
    # render role data in roles.html
    return render_template('roles.html', rows = rows)

  elif request.form['action'] == 'To Admin':
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