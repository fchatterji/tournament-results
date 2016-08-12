# tournament-results

## Description

A simple swiss tournament planner, composed of a database to store the game matches between players and code to query this data and determine the winners of various games.

This project runs a set of tests to confirm that the planner works.

## Getting started

To set up the project
- install Git, Virtual Box and Vagrant. Detailed installation instructions can be found here: https://www.udacity.com/wiki/ud197/install-vagrant
- Download this tournament repository and place it in your /vagrant directory.

In your terminal, run the following commands:
- cd /path/to/vagrant (changes directories to the 'vagrant' directory).
- vagrant up (starts the virtual machine).
- vagrant ssh (creates a remote connection to your virtual machine).
- cd /vagrant/tournament (changes directories to the 'tournament' directory in your virtual machine).
- psql (launches the PostgreSQL interactive terminal).
- \i tournament.sql (this command reads in the sql commands from 'tournament.sql' which will create the 'tournaments' database and the necessary tables and views needed by the application).
- \q (to quit the PostgreSQL interactive terminal).
- python tournament_test_extra.py (this runs the python tests against the tournament.py module.
- 

Results: The test results should be as show below:

- Events can be deleted.
- Old matches can be deleted.
- Player records can be deleted.
- After deleting, countPlayers() returns zero.
- After registering a player, countPlayers() returns 1.
- Players can be registered and deleted.
- Newly registered players appear in the standings with no matches.
- After a match, players have updated standings.
- After one match, players with one win are paired.
- Success! All tests pass!

## Copyright

This project is part of the udacity full stack web developper nano degree (https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). 

It is not licensed.

