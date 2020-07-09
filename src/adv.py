from room import Rooms
from player import Player
from item import Item
import random

# Declare all the rooms

room = {
    'outside':  Rooms("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Rooms("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Rooms("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Rooms("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Rooms("Treasure Chamber", """You've found the long-lost treasure
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
#  Items
item = {
    'scythe': Item('scythe',"""Death comes in many forms, today that can be you!"""),
    'hi-point': Item('hi-point', """Only has one round in it, but hey just beat em with it."""),
    'bottle': Item('bottle', """For the hard on their luck alcholic adventurer"""),
    'alligator': Item('alligator', """Channel your inner Florida man.""")
}
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

player = Player("jake","outside")

is_playing = True

# while is_playing:
#     print(jake.room)
#     print(room[jake.room].description)
#     direction = input("Which way? n,e,s,w")
#     if direction == "n":
#         jake.room = room[jake.room].n_to
#     print(jake.room)
#     is_playing = False

while is_playing:
    print(room[player.room])
    room[player.room].loot = []
    floor_loot = random.choice(list(item))
    room[player.room].add_item(floor_loot)
    print(f'There is a {floor_loot} on the floor')

    
    # TODO: (the textwrap module might be useful here).
    direction = input('Where do you want to go? N, E, S, W? To pickup or drop items use takethe command take "item" or drop "item" To show your inventory enter "i"').lower().split()
    if direction[0] == 'n':
        if player.room == 'outside':
            player.room = 'foyer'
            print(player.room)
        elif player.room == 'foyer':
            player.room ='overlook'
        elif player.room == 'narrow':
            player.room = 'treasure'
        else:
            direction = input('Please choose another direction: S, W, E ')
    elif direction[0] == 'e':
        if player.room == 'foyer':
            player.room = 'narrow'
        else:
            direction = input('Please choose another direction: N, S, W ')
    elif direction[0] == 's':
        if player.room == 'foyer':
            player.room = 'outside'
        elif player.room == 'overlook':
            player.room = 'foyer'
        elif player.room == 'treasure':
            player.room = 'narrow'
        else:
            direction = input('Please choose another direction: N, W, E ')
    elif direction[0] == 'w':
        if player.room == 'narrow':
            player.room = 'foyer'
        else:
            direction = input('Please choose another direction: N, S, E ')
    elif direction[0] == 'q':
        is_playing = False
    elif direction[0] == 'take' or direction[0] == 'get':
        if direction[1] in room[player.room].loot:
            player.add_item(direction[1])
            room[player.room].remove_item(direction[1])
            print(f'You picked up: {direction[1]}')
        else: direction =input('Well clearly you are an idiot! Do you want to try that again?')
    elif direction[0] == 'drop' or direction[0] == 'remove':
        if direction[1] in room[player.room].loot:
            player.drop_item(direction[1])
            room[player.room].add_item(direction[1])
            print(f'You dropped: {direction[1]}')
        else: direction =input('Well clearly you are an idiot! Do you want to try that again?')
    elif direction[0] == 'yeet':
        if direction[1] in player.inventory:
            player.drop_item(direction[1])
            
            print(f'You yeeted: {direction[1]} into another dimension! Thats a win from me dawg!')
            player.room = 'treasure'
        else: direction =input('You have nothing to yeet! RIP')
    elif direction[0] == 'i' or direction[0] == 'inv' or direction[0] == 'inventory':
        direction = input(f'You have the following items: {player.inventory}')

    else:
        direction = input('Please choose a valid direction, or press q to quit')