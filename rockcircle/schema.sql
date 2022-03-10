DROP TABLE IF EXISTS Roles;
CREATE TABLE Roles (
  prole VARCHAR(25),
  pname VARCHAR(25),
  PRIMARY KEY (prole)
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