from rockcircle import app
from rockcircle.db import query_db

NO_SUBMISSION = 'n/a'

def add_player(pname, prole):
  """
  add a player & role to Roles table
  :param pname: player name
  :param prole: player role
  """
  query_db('INSERT INTO Players (prole, pname) VALUES (%s, %s)', (prole, pname))


def cast_vote(pname, pvote, cvote, mvote):
  """
  add a player's vote to the Votes table
  if the current round has the reached number of votes, drop someone
  :param pname: player name
  """
  ROUND = get_current_round()

  # validate that the player hasn't already submitted a vote this round
  vote = get_vote(pname, ROUND)
  if vote != None:
    app.logger.info('player already submitted, vote not counted')
    return 
  
  # validate that player is the captain if they submitted a captain vote
  if cvote != NO_SUBMISSION:
    res = query_db('SELECT pname FROM Players WHERE prole = "CAPTAIN"', one=True)
    cname = res['pname'] if res != None else ''
    if pname != cname:
      app.logger.info('captain vote & player name did not match, vote not counted.')
      return

  # validate that player is the medic if they submitted a medic vote
  if mvote != NO_SUBMISSION:
    res = query_db('SELECT pname FROM Players WHERE prole = "MEDIC"', one=True)
    mname = res['pname'] if res != None else ''
    if pname != mname:
      app.logger.info('medic vote & player name did not match, vote not counted.')
      return
  
  # insert vote into Votes table
  query_db('INSERT INTO Votes VALUES (%s, %s, %s, %s, %s)',
                                     (ROUND, pname, pvote, cvote, mvote))  


def drop_player(pname):
  """
  remove a player from the Roles table
  :param pname: player name
  """
  query_db('DELETE FROM Players WHERE pname = (%s)', (pname,))


def get_num_players():
  """
  get the total number of players left
  """
  return query_db('SELECT COUNT(pname) FROM Players', one=True)[0]


def get_max_round():
  """
  get the maximum noted round in the votes table
  """
  res = query_db('SELECT MAX(round) FROM Votes', one=True) 
  return res[0] if res[0] != None else 0


def get_current_round():
  """
  get the current round
  """
  max_round   = get_max_round()
  num_players = get_num_players()
  sub_players = get_submitted_players()

  if(num_players == len(sub_players)):
    # if all players have submitted, then the current round is the "next" round
    return max_round + 1
  else:
    return max_round


def get_submitted_players():
  """
  get a list of players who've already submitted votes this round
  assumes that this isn't a new round.
  """
  res = query_db('SELECT pname FROM Votes WHERE round = (SELECT MAX(round) FROM Votes)')
  # unpack to dict first to avoid indexing errors
  res = [dict(r) for r in res]
  # unpack dict to list
  res = [d['pname'] for d in res]
  return res


def get_vote(pname, round):
  """
  gets a player's vote for a specific round
  """
  cur_round = get_current_round()

  if round > cur_round:
    return None 
  
  res = query_db('SELECT pvote FROM Votes WHERE pname = (%s) AND round = (%s)', (pname, round), one=True)
  res = res[0] if res != None else None
  return res

def get_results(round):
  """
  get the names & how many votes they received for a given round
  """
  cur_round = get_current_round()

  if round > cur_round:
    return None 

  res = query_db('SELECT pvote, COUNT(*) FROM Votes GROUP BY pvote, cvote')
  
  # unpack to dict to avoid indexing errors
  res = [dict(r) for r in res]

  # rename fields
  final = []
  for d in res:
    renamed_dict = {}
    renamed_dict['name'] = d['pvote']
    renamed_dict['count'] = d['COUNT(*)']
    final.append(renamed_dict)
  return final
