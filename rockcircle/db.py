import sqlite3
from flask import g

"""
Global space for relevant database filenames / paths
"""
DATABASE = 'database.db'
SCHEMA   = 'rockcircle/schema.sql'
ROLES    = 'rockcircle/roles.sql'

def init_db():
  """
  initialize the database by inputting the schema
  """
  # establish database connection
  con = sqlite3.connect(DATABASE)

  # create db from schema
  with open(SCHEMA) as f:
    con.executescript(f.read())

  # init DB with role data
  with open(ROLES) as f:
    con.executescript(f.read())

  con.close()


def get_db():
  """
  get a connection into the database
  :returns: a connection to the database
  """

  db = getattr(g, '_database', None)
  if db is None:
      db = g._database = sqlite3.connect(DATABASE)
  return db

def query_db(query, args=(), one=False):
  """
  send a query to the db and return the result
  :param query: query to be executed
  :param args: argument list to be substituted into the query
  :param one: if True, return only the first row
  :returns: a list of indexable rows
  """
  # establish connection
  con = get_db()

  # set row factory to return row type instead of tuples
  # this allows us to query by key instead of index
  con.row_factory = sqlite3.Row 

  # execute query, store rows in rv
  cur = con.cursor()
  cur.execute(query, args)
  # commit executed query to db in case of INSERT
  con.commit()
  rv = cur.fetchall()

  cur.close()

  # if the one tag is set, return only the first row
  return (rv[0] if rv else None) if one else rv