# Knights-Quest
This fast-paced, two-dimensional game will put your reflexes to the test. It uses coordinates to create a two-dimensional playing area and Pygame Zero's Actor class to introduce the characters and collectable items in the game. An event loop program makes the game run smoothly.
# How to play this game
The aim of this game is to navigate the knight arund the dugeon--a two-dimensional playing area--with the arrow keys, but you cannot move through the walls or the locked door. Collect the keys by moving over them. However, you need to avoid the guards as they try to move toward the knight. Any contact with the guards ends the game. You win if you can get to the door after picking up all of the keys.
# Dungeon crawl
This project is an example of a style of game called dungeon crawl. In such games, the player usually navigates a labyrinthine enviornment, collecting items and battling or avoiding enemies. This game will use classic top-down 2D view, where the player appears to be looking down at the play area from above.
# The scenery
The game is based on a simple grid on which square images called "tiles" are placed. The scenery of the game consists of a background of floor tiles, with additional tiles representing the walls and the door.
Actors in this game are represented by the following:
- Guard: A red sheild with two swords crossing in the middle
- Knight: A yellow knight helmet
- Key: A blue key
# The actors
The movable or collectable items in the game are called actors. In this game, the actors are the same size as the tiles so that each is contained whithin one grid square. They are drawn on top of the scenery so that the background can be seen behind and through them. 
# The Pygame Zero game loop
A Pygame Zero program is an example of an event loop program. An event loop runs continuously, calling other parts of the program when an event occurs so that actions can be taken. The code necessary to manage this loop is part of Pygame Zero, so you only need to write the handler functions that deal withe these events. 
# Set up game
Top-level statements in the Python file will be executed first and can be used to initialize the game state and configure Pygame Zero itself. Pygame Zero will then open a window and repeat the event loop continuously.
# Handle input events
Pygame Zero will check for input events, such as key presses, mouse movements, and button presses each time through the loop. It will call the appropriate handler function when one of these events occurs.
# Update game state
At this point, Pygame Zero allows the user to do any work that they want done on every loop iteration by calling the update handler funciton This ian an optional function.
# Draw interface
Finally, Pygame Zero calls the draw handler function, which will redraw the contnts fo the game window to reflect the current game state.
