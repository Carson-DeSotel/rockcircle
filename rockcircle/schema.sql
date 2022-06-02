/**
 * Manage the Roles including their name, allegiance, and description
 * rname: the name of the role
 * rteam: the allegiance of the role {PASSENGERS, STOWAWAYS}
 * rdesc: a short description of the roles
 */ 
DROP TABLE IF EXISTS Roles CASCADE;
CREATE TABLE Roles (
  rname VARCHAR(25),
  rteam VARCHAR(25),
  rdesc VARCHAR(256),
  PRIMARY KEY (rname)
);

/**
 * Manage any players that are playing the game.
 * pname: the player's name
 * prole: the role that the player has been assigned
 * align: the player's alignment; either {PASSENGERS, STOWAWAYS} 
 *  - this field is needed for the GHOST & TURNCOAT
 * This schema should avoid naming conflicts should there be 
 * multiple people with the same name, as the roles are unique and the 
 * combination of the name and role should be exclusive.
 */
DROP TABLE IF EXISTS Players;
CREATE TABLE Players (
  pname VARCHAR(25),
  prole VARCHAR(25),
  align VARCHAR(25),
  PRIMARY KEY (pname, prole),
  FOREIGN KEY (prole) REFERENCES Roles(rname)
);

/**
 * Store the rooms in play and their rank.
 * rname: the name of the room
 *   - defaults to numerics, can be changed by the user
 * rrank: the rank of the room; determines the order in which they're
 *        removed from play
 */
DROP TABLE IF EXISTS Rooms;
CREATE TABLE Rooms (
  rname VARCHAR(25),
  rrank INTEGER,
  PRIMARY KEY (rname)
);

/**
 * Store the cast votes for every round.
 * round: the round the vote was cast in
 * pname: the name of the player whose vote was cast
 * prole: the role of the player whose vote was cast
 * pvote: the person the player voted for
 * extra: if the player has an extra action due to their role, 
          display the value submitted
 */
DROP TABLE IF EXISTS Votes;
CREATE TABLE Votes (
  round VARCHAR(2),
  pname VARCHAR(25),
  pvote VARCHAR(25),
  extra VARCHAR(25),
  PRIMARY KEY (round, pname)
);