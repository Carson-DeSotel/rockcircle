""" Database Functions

This file contains relevant functions for 
* establishing connections to the database
* closing connections
* querying the database
* initializing the database according to specified SQL files

This file also contains definitions for pre-defined SQL files
noted in the global space.
"""

import psycopg2
import psycopg2.extras

"""
Global space for relevant database filenames / paths
"""
SCHEMA   = 'rockcircle/schema.sql'
ROLES    = 'rockcircle/roles.sql'
SCRIPTS  = [SCHEMA, ROLES]


def db_connect():
  # establish database connection
  conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='postgres',
    # connect to db host due to being in a different Docker image
    host='db',
    # switch to DictCursor to allow access by field
    cursor_factory=psycopg2.extras.DictCursor,
  )
  return conn


def db_close(conn):
  """
  close the database connection and cursor
  :param conn: connection to the database to close
  """
  # get cursor so that we can close it
  cur = conn.cursor()

  # close cursor & connection
  cur.close()
  conn.close()


def init_db():
  """
  initialize the database by inputting the specified schema
  """
  conn = db_connect()

  # obtain cursor from connection
  cur = conn.cursor()

  # load in each SQL script
  for script in SCRIPTS:
    with open(script) as f:
      cur.execute(f.read())

  # commit changes
  conn.commit()

  db_close(conn)


def query_db(query, args=(), one=False):
  """
  send a query to the db and return the result
  :param query: query to be executed
  :param args: argument list to be substituted into the query
  :param one: if True, return only the first row
  :returns: a list of indexable rows
  """
  # establish connection
  conn = db_connect()

  # execute query, store rows in rv
  cur = conn.cursor()
  cur.execute(query, args)

  # commit executed query to db in case of INSERT
  conn.commit()

  # get results back from SELECT queries
  if cur.description is not None:
    res = cur.fetchall()
    
    # close connection
    db_close(conn)

    # if the one tag is set, return only the first row
    return (res[0] if res else None) if one else res

  # just close if there's no data to get  
  else:
    db_close(conn)
    return None
