#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import rooms
rooms = rooms.rooms

print(rooms)
def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')
    print('To win: bring the key and the potion to the garden! Avoid the monsters!')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

# an initially empty inventory list
inventory = []


# start the player in the Entrance
currentRoom = 'Entrance'

showInstructions()

# breaking this loop means the game is over
while True:
    showStatus()

    # the player must type something in otherwise they will be prompted again
    move = ''
    while move == '':
        move = input('>')

    # normalize the input
    move = move.lower().split(" ", 1)
    if move[0] == 'go':
        # check of the move is allowed
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        # if they are not allowed
        else: 
            print("You can\'t go that way!")
        # if they type 'get' first
    if move[0] == 'get':
        # check if current room contains and item and if the item matches what the player wants
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add to invy
            inventory.append(move[1])
            # display msg
            print(move[1] + ' got!')
            # delete the item kv pair from room dict
            del rooms[currentRoom]['item']
            # if there's no item in the room or the item doesn't match
        else:
            print("Can\'t get " + move[1] + "!")
            # if the player finds a monster, they lose
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
                print("A monster has got you... GAME OVER!")
                break
            # win condition
            if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
                print("You escaped the house with the ultra rare key and magic potion... YOU WIN!")
                break
