from room import Room
# from item import Item
from player import Player
# import textwrap

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
# player = Player(room['outside'])
player = Player(input("What is your name?: "), room["outside"])


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

while True:
    print(player.current_room)
    cmd = input("-> ").lower()
    if cmd in ["n", "e", "s", "w"]:
        current_room = player.current_room
        next_room = getattr(current_room, f"{cmd}_to")
        if next_room is not None:
            player.current_room = next_room
        else:
            print("Nothing there")
    elif cmd == "q":
        print("Byye!")
        exit()
    else:
        print("invalid entry, please try again.")
        







































































































































































































""""
# while True:
#     #key command input
#     cmd = input("To Move between rooms, please use: 'n', 'e', 's', 'w': \n~~~>").lower()
#     if cmd in ["n", "e", "s", "w"]:
#         #moves player to that room
#         player.travel(cmd)
#     elif cmd == "q":
#         print("See you next time!")
#         exit()
#     else:
#         print("Please enter a direction to Move or 'q' Quit.")
""""