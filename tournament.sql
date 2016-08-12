-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- create the tournament database and connect to it
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- one table for players, with id and name
CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
);

-- one table for matches, with id, player win (fk), player lose (fk)
CREATE TABLE matches (
    id serial PRIMARY KEY,
    winner_id int REFERENCES players(id),
    loser_id int REFERENCES players(id)
);

CREATE VIEW v_wins as 
        SELECT winner_id, count(*) as wins
        FROM matches
        GROUP BY winner_id;

CREATE VIEW v_players_wins as
        SELECT id, name, COALESCE(wins,0) as wins
        FROM players LEFT JOIN v_wins
        ON players.id = v_wins.winner_id;

CREATE VIEW v_losses as 
        SELECT loser_id, count(*) as losses
        FROM matches
        GROUP BY loser_id;

CREATE VIEW v_players_losses as
        SELECT id, name, COALESCE(losses,0) as losses
        FROM players LEFT JOIN v_losses
        ON players.id = v_losses.loser_id;

CREATE VIEW v_standings as
        SELECT v_players_wins.id, v_players_wins.name, wins, wins+losses as matches
        FROM v_players_wins LEFT JOIN v_players_losses
        ON v_players_wins.id = v_players_losses.id
        ORDER BY wins DESC;


INSERT INTO players(name) values ('joe');
INSERT INTO players(name) values ('ian');
INSERT INTO players(name) values ('alfred');
INSERT INTO players(name) values ('gustav');
INSERT INTO players(name) values ('jill');

INSERT INTO matches(winner_id, loser_id) values (1, 2);
INSERT INTO matches(winner_id, loser_id) values (3, 4);
INSERT INTO matches(winner_id, loser_id) values (1, 3);
INSERT INTO matches(winner_id, loser_id) values (4, 2);
