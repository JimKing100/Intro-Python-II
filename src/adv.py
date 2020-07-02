from room import Room
from player import Player


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
program = 0
command_verbs = {'n', 's', 'e', 'w', 'q'}
current_room = room['outside']
player1 = Player('Jim', current_room)

print(player1.name, '-', current_room.name, ' - ', current_room.description)

while program == 0:
    move = input('Enter a direction to move n, s, e, w or q to quit: ')
    error_code = 0

    if move in command_verbs:
        if (move == 'n') & (current_room.n_to is not None):
            current_room = current_room.n_to
        elif (move == 'n') & (current_room.n_to is None):
            error_code = 1
        if (move == 's') & (current_room.s_to is not None):
            current_room = current_room.s_to
        elif (move == 's') & (current_room.s_to is None):
            error_code = 1
        if (move == 'e') & (current_room.e_to is not None):
            current_room = current_room.e_to
        elif (move == 'e') & (current_room.e_to is None):
            error_code = 1
        if (move == 'w') & (current_room.w_to is not None):
            current_room = current_room.w_to
        elif (move == 'w') & (current_room.w_to is None):
            error_code = 1

        if error_code == 0:
            player1.current_room = current_room
            print(player1.name, '-', current_room.name, ' - ', current_room.description)
        else:
            print('There is no room in this direction!')
        if move == 'q':
            program = 1

    else:
        print('Invalid input - n, s, e, w, q are valid commands')
