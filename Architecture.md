Here is explained the architecture of the project.
There are 2 main objectives for the program: 
* Simulate a match and display it in 2D.
* Generate the best strategy using a genetic algorithm.

Simulate a match
----------------
This means we want to represent each zone of the table, with game elements and 
robots that can move/be moved. Some specific actions that the robot can do and
that some zone of the table has, for example: push the gift on the side of the table.

Generate a strategy with a genetic algorithm
--------------------------------------------
In order to do this, we need to have a good representation of the state of table
and of the possible moves and actions that can be done. We don't want to forget
that the game is adversarial so we need to have 2 strategies fighting each other.


Model of the world
------------------
Here we want to have good data structures to represent the world.
It is composed of the following items:
* A Table: the background
* zones on the table: can contain items, or robots.
* Elements (or items) of gaming: that can be moved around the table
* Table actions: static things to change on the table
* Robots: can move and interact with the world
* A color: the side of the table where you begin, your team
* The points: for each action/item.
* The total score: sum of the points for each team



Representation in 2D
--------------------



Good combinations for a genetic algorithm
-----------------------------------------