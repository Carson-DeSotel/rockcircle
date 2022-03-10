from rockcircle.db import query_db

def add_player(pname, prole):
  """
  add a player & role to Roles table
  :param pname: player name
  :param prole: player role
  """
  query_db('INSERT INTO Roles (prole, pname) VALUES (?, ?)', (prole, pname))

def cast_vote(pname):
  """
  add a player's vote to the Votes table
  if the current round has the reached number of votes, drop someone
  :param pname: player name
  """
  pass

def drop_player(pname):
  """
  remove a player from the Roles table
  :param pname: player name
  """
  query_db('DELETE FROM Roles WHERE pname = ?', (pname,))
