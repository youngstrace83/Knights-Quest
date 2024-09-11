# Imports the Pygame Zero functionality
import pgzrun

# Defines the width and height of the game grid and the size of each tile
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

# Defines the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# Define's the scenery where W = Wall, K = Key, G = Guard, P = Player and D = Door
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]
# This function converts a grid position to screen coordinates 
def screen_coords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def grid_coords(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE)) # Determines the position of an actor on the grid

def setup_game():
    global player # Defines player as a global variable
    player = Actor("player", anchor=("left", "top")) # Creates a new Actor object and sets its anchor position
    for y in range(GRID_HEIGHT): # Loops over each grid position
        for x in range(GRID_WIDTH): 
            square = MAP[y][x] # Extracts the character from the map representing this grid position
            if square == "P": # Checks if this grid position is the player
                player.pos = screen_coords(x, y) # Sets the position of player to the screen coordinates of the grid position

def draw_background():
    for y in range(GRID_HEIGHT): # Loops over each grid row
        for x in range(GRID_WIDTH): # Loops over each grid column
            screen.blit("floor1", screen_coords(x, y)) # screen.blit() draws the named image at the given screen position
def draw_scenery():
    # Loops over each grid position
    for y in range(GRID_HEIGHT): 
        for x in range(GRID_WIDTH): 
            square = MAP[y][x] # Extracts the character from the map represented by this grid position
            if square == "W": # Draws a wall tile at the screen position represented by W
                screen.blit("wall", screen_coords(x, y))
            elif square == "D": # Drwas the door tile at position D
                screen.blit("door", screen_coords(x, y))

def draw_actors():
    player.draw() # Drows the player actor onscreen at it's current position

# The draw handler function is called automatically from the game loop
def draw():
    draw_background() # Draws the dungeon floor as a background onscreen
    draw_scenery() # Draws the scenery after (on top of) the background has been drawn
    draw_actors() # Drwas the actors after (on top of) the background and scenery have been drawn

def on_key_down(key): # Reacts when the user presses down on a key
    if key == keys.LEFT: 
        move_player(-1, 0) # Player moves left by one grid square
    elif key == keys.UP:
        move_player(0, -1) # Player moves up by one grid square
    elif key == keys.RIGHT:
        move_player(1, 0) # Player moves right by one grid square
    elif key == keys.DOWN:
        move_player(0, 1) # Player moves down by one grid Square

def move_player(dx, dy)
    (x, y) = grid_coords(player) # Gets the current grid position of player
    x += dx # Adds the x axis distance to x
    y += dy # Adds the y axis distance to y
    square = MAP[y][x] # Gives the tile at this position
    if square == "W":
        return # Stops the execution of the move_player() function, if the player touches the wall
    elif square == "D":
        return # Returns immediately if it is a door
    player.pos = screen_coords(x, y) # Updates position of player to the new coordinates

setup_game()
# Starts Pygame Zero
pgzrun.go()
