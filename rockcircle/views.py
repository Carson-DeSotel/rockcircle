from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db
from rockcircle.game import add_player, drop_player

@app.route('/', methods=['GET', 'POST'])
def index():
  """
  handles all requests coming into the main page '/'
  includes adding players, casting votes, etc.
  """
  # read POST request from form data
  if request.method == 'POST':
    # identify which submit was pressed based on HTML button value attr.
    if request.form['action'] == 'Add Player':
      # get name & role from text fields, send to UPPERCASE
      pname = request.form.get('pname').upper()
      prole = request.form.get('prole').upper()

      # add name & role to database
      add_player(pname, prole)

    elif request.form['action'] == 'To Vote':
      # get all names and pass them into votes
      rows = query_db('SELECT pname FROM Roles')
      return render_template('vote.html', rows = rows)
      
    elif request.form['action'] == 'Cast Vote':
      # read name from radio buttons
      pname = request.form['name']
      print('VOTED OFF:', pname)
      drop_player(pname)

  return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
  """
  handle some admin features for debug purposes
  """
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