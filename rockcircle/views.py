from flask import g, render_template, request, redirect, url_for

from rockcircle import app
from rockcircle.db import get_db, query_db
from rockcircle.game import (add_player, cast_vote, 
                             get_num_players, NO_SUBMISSION,
                             get_current_round,
                             get_submitted_players,
                             get_results)

@app.route('/', methods=['GET', 'POST'])
def index():
  """
  handles all requests coming into the main page '/'
  includes adding players, casting votes, etc.
  """
  # read POST request from form data
  if request.method == 'POST':
    # identify which submit was pressed based on HTML button value attr.
    if request.form.get('action') == 'Add Player':
      # get name & role from text fields, remove whitespace, send to UPPERCASE
      pname = request.form.get('pname').strip().upper()
      prole = request.form.get('prole').strip().upper()
      
      app.logger.info('Adding Player: ' + pname + ' ' + prole)
      # add name & role to database
      add_player(pname, prole)

    elif request.form.get('action') == 'To Vote':
      # get all names and pass them into votes
      rows = query_db('SELECT pname FROM Roles')
      return render_template('vote.html', rows = rows)
      
    elif request.form.get('action') == 'Cast Vote':
      # read name from radio buttons
      pname = request.form.get('pname')
      pvote = request.form.get('pvote')
      cvote = request.form.get('cvote', NO_SUBMISSION)
      mvote = request.form.get('mvote', NO_SUBMISSION)

      # log each vote submitted
      app.logger.info('Vote Submitted: ' + ' '.join((pname, pvote, cvote, mvote)))
      cast_vote(pname, pvote, cvote, mvote)

    elif request.form.get('action') == 'To Results':
      cur_round = get_current_round()
      results = get_results(cur_round)
      return render_template('results.html', results = results)

    elif request.form.get('action') == 'To Index':
      return render_template('index.html')

  return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
  """
  handle some admin features for debug purposes
  """

  num_players = get_num_players()
  cur_round   = get_current_round()
  sub_players = get_submitted_players()
  results = get_results(cur_round)

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
    return render_template('admin.html', num_players = num_players,
                                         cur_round   = cur_round,
                                         sub_players = sub_players,)

  else:
    return render_template('admin.html', num_players = num_players,
                                         cur_round   = cur_round,
                                         sub_players = sub_players,)
@app.teardown_appcontext
def close_connection(exception):
  """
  close down the database as the app is being closed
  """
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()