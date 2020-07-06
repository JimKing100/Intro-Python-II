# An Adventure Game

# Imports
from room import Room
from player import Player
from item import Treasures
from item import LightSource
from item import Weapons


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, west and east."""),

    'grotto': Room("Grotto", """A beautiful cave-like room, bright sunlight beams
through a doorway to the south."""),

    'sunroom': Room("Sun Room", """A window-filled room, bright sunlight streams
through the windows, the only exit is to the north."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! It is filled with treasure, but no diamonds. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].w_to = room['grotto']
room['foyer'].e_to = room['narrow']
room['grotto'].e_to = room['foyer']
room['grotto'].s_to = room['sunroom']
room['sunroom'].n_to = room['grotto']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create items
coins = Treasures('coins', 'a hundred ducats', 100)
gold = Treasures('gold', 'a bar of gold', 200)
silver = Treasures('silver', 'a bar of silver', 100)
diamonds = Treasures('diamonds', 'a bag of diamonds', 200)

lamp = LightSource('lamp', 'a gas lamp')
flashlight = LightSource('flashlight', 'a large flashlight')
torch = LightSource('torch', 'an oil torch')

sword = Weapons('sword', 'the sword of zorro')
crossbow = Weapons('crossbow', 'a crossbow with arrows')
knife = Weapons('knife', 'a bowie knife')
club = Weapons('club', 'a large wooden club')

# Add items to rooms
room['outside'].add_item(sword)
room['outside'].add_item(torch)
room['foyer'].add_item(crossbow)
room['foyer'].add_item(flashlight)
room['narrow'].add_item(lamp)
room['treasure'].add_item(silver)
room['treasure'].add_item(gold)
room['grotto'].add_item(coins)
room['grotto'].add_item(club)
room['sunroom'].add_item(diamonds)
room['overlook'].add_item(knife)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# A loop that does the following:
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
command_verbs = {'n', 's', 'e', 'w', 'i', 'q', 'get', 'take', 'drop', 'inventory', 'score'}
current_room = room['outside']
player1 = Player('Player 1', current_room)

print(player1.name, '-', current_room.name, ' - ', current_room.description)
print('Items visible:')
for item in current_room.list:
    print(item.name)

while program == 0:
    entry_text = input('Enter a command (n,s,e,w,i,q,get [item],take [item],drop [item],inventory,score): ')
    words = entry_text.split()

    command = ' '
    if len(words) == 1:
        command = words[0]
    if len(words) == 2:
        command = words[0]
        object = words[1]

    error_code = 0

    if command in command_verbs:
        if (command == 'n') & (current_room.n_to is not None):
            current_room = current_room.n_to
        elif (command == 'n') & (current_room.n_to is None):
            error_code = 1
        if (command == 's') & (current_room.s_to is not None):
            current_room = current_room.s_to
        elif (command == 's') & (current_room.s_to is None):
            error_code = 1
        if (command == 'e') & (current_room.e_to is not None):
            current_room = current_room.e_to
        elif (command == 'e') & (current_room.e_to is None):
            error_code = 1
        if (command == 'w') & (current_room.w_to is not None):
            current_room = current_room.w_to
        elif (command == 'w') & (current_room.w_to is None):
            error_code = 1
        if (command == 'i') | (command == 'inventory'):
            if not player1.list:
                print(player1.name, 'has no items')
            else:
                print(player1.name, 'has these items:')
                for item in player1.list:
                    if item.isTreasure() is True:
                        print(item.name, 'value is', item.value)
                    else:
                        print(item.name)
        if (command == 'get') | (command == 'take'):
            for item in current_room.list:
                if item.name == object:
                    player1.add_item(item)
                    current_room.remove_item(item)
                    item.on_take()
                    break
                else:
                    print('No such object in this room')
        if (command == 'drop'):
            for item in player1.list:
                if item.name == object:
                    current_room.add_item(item)
                    player1.remove_item(item)
                    item.on_drop()
                    break
                else:
                    print('No such object in inventory')
        if (command == 'score'):
            print('To win you must score 400 points, you have', player1.score, 'points')

        if error_code == 0:
            player1.current_room = current_room
            print(player1.name, '-', current_room.name, ' - ', current_room.description)
            if not current_room.list:
                print('There are no items visible')
            else:
                print('Items visible:')
                for item in current_room.list:
                    if item.isTreasure() is True:
                        print(item.name, 'value is', item.value)
                    else:
                        print(item.name)
        else:
            print('There is no room in this direction!')
        if command == 'q':
            program = 1

    else:
        print('Invalid input - n,s,e,w,i,q,get item,take item,drop item,inventory are valid commands')
