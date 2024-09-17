# Imports the Pygame Zero functionality
import pgzrun
import random

# Defines the width and height of the game grid and the size of each tile
GRID_WIDTH = 20
GRID_HEIGHT = 15
GRID_SIZE = 50
GUARD_MOVE_INTERVAL = 0.5
PLAYER_MOVE_INTERVAL = 0.1
BACKGROUND_SEED = 123456
PLAYER_MOVE_INTERVAL = 0.25

# Defines the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# Define's the scenery where W = Wall, K = Key, G = Guard, P = Player and D = Door
MAP = ["WWWWWWWWWWWWWWWWWWWW",
       "W        W         W",
       "W        W         W",
       "W   W        W     D",
       "W   W G K    W     W",
       "W   WWWWWWWWWWWW   W",
       "W                  W",
       "W                  W",
       "W   WWWWW  WWWWW   W",
       "W   W      W  KW   W",
       "W   W P    WG  W   W",
       "W   WWWWWWWW   W   W",
       "W     G            W",
       "W     K            W",
       "WWWWWWWWWWWWWWWWWWWW"]
# This function converts a grid position to screen coordinates 
def screen_coords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def grid_coords(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE)) # Determines the position of an actor on the grid

def setup_game():
    global game_over, player_won, player, keys_to_collect, guards # Defines game_over, player_won, player, guards and keys_to_collect as a global variables
    game_over = False # Sets the variable to False initially
    player_won = False
    player = Actor("player", anchor=("left", "top")) # Creates a new Actor object and sets its anchor position
    keys_to_collect = [] # Sets keys_to_collect to an empty list initially
    guards = [] # Sets guards to an empty list initially
    for y in range(GRID_HEIGHT): # Loops over each grid position
        for x in range(GRID_WIDTH): 
            square = MAP[y][x] # Extracts the character from the map representing this grid position
            if square == "P": # Checks if this grid position is the player
                player.pos = screen_coords(x, y) # Sets the position of player to the screen coordinates of the grid position
            elif square == "K": # Creates a key if the square is K
                key = Actor("key", anchor=("left", "top"), pos=screen_coords(x, y)) # Creates the key actor with an image, anchor, and position
                keys_to_collect.append(key) # Adds this actor to the list of keys created above
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"), pos=screen_coords(x, y))
                guards.append(guard)

def draw_background():
    random.seed(BACKGROUND_SEED)
    for y in range(GRID_HEIGHT): # Loops over each grid row
        for x in range(GRID_WIDTH): # Loops over each grid column
            if x % 2 == y % 2:
                screen.blit("floor1", screen_coords(x, y)) # screen.blit() draws the named image at the given screen position
            else:
                screen.blit("floor2", screen_coords(x, y))
            n = random.randint(0, 99)
            if n < 5:
                screen.blit("crack1", screen_coords(x, y))
            elif n < 10:
                screen.blit("crack2", screen_coords(x, y))
def draw_scenery():
    # Loops over each grid position
    for y in range(GRID_HEIGHT): 
        for x in range(GRID_WIDTH): 
            square = MAP[y][x] # Extracts the character from the map represented by this grid position
            if square == "W": # Draws a wall tile at the screen position represented by W
                screen.blit("wall", screen_coords(x, y))
            elif square == "D" and len(keys_to_collect) > 0: # Drwas the door tile at position D
                screen.blit("door", screen_coords(x, y))

def draw_actors():
    player.draw() # Drows the player actor onscreen at it's current position
    for key in keys_to_collect: # Draws all the actors in the list keys_to_collect
        key.draw()
    for guard in guards:
        guard.draw() # Draws all the actors in the list guards

def draw_game_over():
    screen_middle = (WIDTH / 2, HEIGHT /2) # Sets the position of the "GAME OVER" message onscreen
    screen.draw.text("GAME OVER", midbottom=screen_middle, fontsize=GRID_SIZE, color="cyan", owidth=1) # Draws text "GAME OVER" in the middle of the screen
    if player_won:
        screen.draw.text("You won!", midtop=screen_middle, fontsize=GRID_SIZE, color="green", owidth=1)
    else:
        screen.draw.text("You lost!", midtop=screen_middle, fontsize=GRID_SIZE, color="red", owidth=1)
    screen.draw.text("Press SPACE to play again", midtop=(WIDTH /2, HEIGHT /2 + GRID_SIZE), fontsize=GRID_SIZE /2, color="cyan", owidth=1)

# The draw handler function is called automatically from the game loop
def draw():
    draw_background() # Draws the dungeon floor as a background onscreen
    draw_scenery() # Draws the scenery after (on top of) the background has been drawn
    draw_actors() # Drwas the actors after (on top of) the background and scenery have been drawn
    if game_over:
        draw_game_over()

def on_key_up(key):
    if key == keys.SPACE and game_over:
        setup_game()

def on_key_down(key): # Reacts when the user presses down on a key
    if key == keys.LEFT: 
        move_player(-1, 0) # Player moves left by one grid square
    elif key == keys.UP:
        move_player(0, -1) # Player moves up by one grid square
    elif key == keys.RIGHT:
        move_player(1, 0) # Player moves right by one grid square
    elif key == keys.DOWN:
        move_player(0, 1) # Player moves down by one grid Square

def move_player(dx, dy):
    global game_over, player_won
    if game_over: # Checks if game_over is set
        return
    (x, y) = grid_coords(player) # Gets the current grid position of player
    x += dx # Adds the x axis distance to x
    y += dy # Adds the y axis distance to y
    square = MAP[y][x] # Gives the tile at this position
    if square == "W":
        return # Stops the execution of the move_player() function, if the player touches the wall
    elif square == "D":
        if len(keys_to_collect) > 0:
            return # Returns immediately if list is not empty
        else: # Checks if all of the keys have been picked up
            game_over = True # Sets game_over to True and continues the move
            player_won = True # Sets it to True when the player wins the game
    for key in keys_to_collect: # Loops over each of the key actors in the list
        (key_x, key_y) = grid_coords(key) # Gets the grid position of a key actor
        if x == key_x and y == key_y: # Checks if the new player position matches the key position
            keys_to_collect.remove(key) # Removes this key from the list if player position matches key position
            break # Breaks out of the for loop, as each square can only contain one key
    animate(player, pos = screen_coords(x, y), duration=PLAYER_MOVE_INTERVAL, on_finished=repeat_player_move) # Updates position of player to the new coordinates

def repeat_player_move():
    if keyboard.left:
        move_player(-1, 0)
    elif keyboard.up:
        move_player(0, -1)
    elif keyboard.right:
        move_player(1, 0)
    elif keyboard.down:
        move_player(0, 1)

def move_guard(guard):
    global game_over
    if game_over:
        return
    (player_x, player_y) = grid_coords(player) # Gets the grid posit of the player actor
    (guard_x, guard_y) = grid_coords(guard) # Gets the grid posit of this guard actor
    if player_x > guard_x and MAP[guard_y][guard_x + 1] != "W":
        guard_x += 1 # Increases the guard's x grid position by 1 if the above condition is true
    elif player_x < guard_x and MAP[guard_y][guard_x - 1] != "W": # Checks if player is to the left of the guard
        guard_x -= 1
    elif player_y > guard_y and MAP[guard_y + 1] [guard_x] != "W":
        guard_y += 1
    elif player_y < guard_y and MAP[guard_y - 1] [guard_x] != "W":
        guard_y -= 1
    animate(guard, pos = screen_coords(guard_x, guard_y), duration=GUARD_MOVE_INTERVAL) # Updates the guard actor's posit to the screen coordinates of the (possibly updated) grid position
    if guard_x == player_x and guard_y == player_y: # Ends the game if the guard's grid posit is the same as the player's grid posit
        game_over = True

def move_guards():
    for guard in guards: # Loops through each guard actor in guards list
        move_guard(guard) # Moves all the guard actors in the list

setup_game()
clock.schedule_interval(move_guards, GUARD_MOVE_INTERVAL) # Schedules regular calls to the move_guard() function
pgzrun.go() # Starts Pygame Zero
