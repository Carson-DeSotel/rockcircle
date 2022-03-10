from rockcircle.db import query_db

def add_player(pname, prole):
  query_db('INSERT INTO Roles (prole, pname) VALUES (?, ?)', (prole, pname))

def drop_player(pname):
  query_db('DELETE FROM Roles WHERE pname = ?', (pname,))
