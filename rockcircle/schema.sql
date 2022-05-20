DROP TABLE IF EXISTS Players;
CREATE TABLE Players (
  prole VARCHAR(25),
  pname VARCHAR(25),
  PRIMARY KEY (prole, pname)
);

DROP TABLE IF EXISTS Votes;
CREATE TABLE Votes (
  round INTEGER,
  pname VARCHAR(25),
  pvote VARCHAR(25),
  cvote VARCHAR(25),
  mvote VARCHAR(25),
  PRIMARY KEY (round, pname)
);

DROP TABLE IF EXISTS Roles;
CREATE TABLE Roles (
  rname VARCHAR(25),
  rteam VARCHAR(25),
  rdesc VARCHAR(128),
  PRIMARY KEY (rname)
);