from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db
from rockcircle.game import add_player, cast_vote, NO_SUBMISSION

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
      # get name & role from text fields, remove whitespace, send to UPPERCASE
      pname = request.form.get('pname').strip().upper()
      prole = request.form.get('prole').strip().upper()
      
      app.logger.info('Adding Player: ' + pname + ' ' + prole)
      # add name & role to database
      add_player(pname, prole)

    elif request.form['action'] == 'To Vote':
      # get all names and pass them into votes
      rows = query_db('SELECT pname FROM Roles')
      return render_template('vote.html', rows = rows)
      
    elif request.form['action'] == 'Cast Vote':
      # read name from radio buttons
      pname = request.form.get('pname')
      pvote = request.form.get('pvote')
      cvote = request.form.get('cvote', NO_SUBMISSION)
      mvote = request.form.get('mvote', NO_SUBMISSION)

      # log each vote submitted
      app.logger.info('Vote Submitted: ' + ' '.join((pname, pvote, cvote, mvote)))
      cast_vote(pname, pvote, cvote, mvote)

  return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
  """
  handle some admin features for debug purposes
  """
  if request.form.get('action') == 'To Roles':
    # get role data from database
    rows = query_db('SELECT * FROM Roles')
    # render role data in db_roles.html
    return render_template('db_roles.html', rows = rows)

  elif request.form.get('action') == 'To Votes':
    # get vote data from database
    rows = query_db('SELECT * FROM Votes')
    # render vote data in db_votes.html
    return render_template('db_votes.html', rows = rows)

  elif request.form.get('action') == 'To Admin':
    return render_template('admin.html')

  else:
    return render_template('admin.html')

@app.teardown_appcontext
def close_connection(exception):
  """
  close down the database as the app is being closed
  """
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()