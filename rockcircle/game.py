from rockcircle.db import query_db

NO_SUBMISSION = 'n/a'
ROUND = 0

def add_player(pname, prole):
  """
  add a player & role to Roles table
  :param pname: player name
  :param prole: player role
  """
  query_db('INSERT INTO Roles (prole, pname) VALUES (?, ?)', (prole, pname))


def cast_vote(pname, pvote, cvote, mvote):
  """
  add a player's vote to the Votes table
  if the current round has the reached number of votes, drop someone
  :param pname: player name
  """
  
  if cvote != NO_SUBMISSION:
    # validate that player is the captain
    cname = query_db('SELECT pname FROM Roles WHERE prole = "CAPTAIN"', one=True)['pname']
    if pname != cname:
      print('pname:', pname)
      print('cname:', cname)
      print('captain vote & player name did not match, vote not counted.')
      return

  if mvote != NO_SUBMISSION:
    # validate that player is the medic
    mname = query_db('SELECT pname FROM Roles WHERE prole = "MEDIC"', one=True)['pname']
    if pname != mname:
      print('pname:', pname)
      print('mname:', mname)
      print('medic vote & player name did not match, vote not counted.')
      return
  
  # insert vote into Votes table
  query_db('INSERT INTO Votes VALUES (?, ?, ?, ?, ?)', (ROUND, pname, pvote, cvote, mvote))
  print('Vote Added')
  


def drop_player(pname):
  """
  remove a player from the Roles table
  :param pname: player name
  """
  query_db('DELETE FROM Roles WHERE pname = ?', (pname,))
