#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        connection = psycopg2.connect("dbname={}".format(database_name))
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("Failure to connect to the database")


def deleteMatches():
    """Remove all the match records from the database."""
    connection, cursor = connect()
    query = "DELETE FROM matches;"
    cursor.execute(query)
    connection.commit()
    connection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    connection, cursor = connect()
    query = "DELETE FROM players;"
    cursor.execute(query)
    connection.commit()
    connection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    connection, cursor = connect()
    query = "SELECT count(*) FROM players;"
    cursor.execute(query)

    count_of_players = cursor.fetchone()[0]

    connection.close()

    return count_of_players


def registerPlayer(name):
    """Add a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connection, cursor = connect()
    query = "INSERT INTO players (name) values (%s);"
    params = (name,)
    cursor.execute(query, params)
    connection.commit()
    connection.close()


def playerStandings():
    """Return a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection, cursor = connect()
    query = "SELECT * FROM v_standings;"
    cursor.execute(query)

    standings = cursor.fetchall()

    connection.close()

    return standings


def reportMatch(winner, loser):
    """Record the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection, cursor = connect()
    query = "INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);"
    params = (winner, loser) 
    cursor.execute(query, params)

    connection.commit()
    connection.close()


def swissPairings():
    """Return a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    # standings includes the player id, name, wins and matches. Here
    # we select only the player id and name.
    standings = [(standing[0], standing[1]) for standing in standings]

    #  pair alternate players from the player standings table
    # to get a list of ((id1, name1), (id2, name2)) tuples
    evens = standings[0::2]
    odds = standings[1::2]
    pairings = zip(evens, odds)

    # concatenate the first and second player for each pairing
    # to get a list of (id1, name1, id2, name2) tuples
    pairings = [pairing[0] + pairing[1] for pairing in pairings]

    return pairings
