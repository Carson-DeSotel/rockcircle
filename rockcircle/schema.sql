DROP TABLE IF EXISTS Roles;
CREATE TABLE Roles (
  prole VARCHAR(25),
  pname VARCHAR(25),
  PRIMARY KEY (prole)
);


DROP TABLE IF EXISTS Votes;
CREATE TABLE Votes (
  pname VARCHAR(25),
  pvote VARCHAR(25),
  prole VARCHAR(25),
  cvote VARCHAR(25),
  medic VARCHAR(25),
  FOREIGN KEY (prole) REFERENCES Roles(prole),
  PRIMARY KEY (pname, prole)
);