#!/usr/bin/env python3

""" Program for simulating kills at Nex, a boss in Oldschool Runescape """

import random
NEX_ITEM_DROP_RATE = 43
NEX_PET_RATE = 500
# if the user recieves a drop, a random int between 1-12 is rolled for weight to decide the drop
NEX_DROP_TABLE_DICTIONARY = {
        "1" : "Torva Helm",
        "2" : "Torva Helm",
        "3" : "Torva Platebody",
        "4" : "Torva Platebody",
        "5" : "Torva Platelegs",
        "6" : "Torva Platelegs",
        "7" : "Nihil Horn",
        "8" : "Nihil Horn",
        "9" : "Zaryte Vambraces",
        "10" : "Zaryte Vambraces",
        "11" : "Zaryte Vambraces",
        "12" : "Ancient hilt"
        }
player_inventory = []
def main():
    play_again = True
    while play_again:
        # welcome message
        welcome()
        # select team size
        while True:
            team_size = input("How many players are on the team? Select 3-50\n")
            if team_size.isdigit():
                team_size = int(team_size)
                if team_size < 3:
                    print("Please select a team size greater than 2")
                elif team_size > 50:
                    print("Please select a team size less than 50")
                else:
                    break;
            else:
                print("Please input an integer between 3 and 50\n")
        # select how many kills
        while True:
            kill_count = input("How many kills would you like to simulate? Select a positive integer\n")
            if kill_count.isdigit():
                kill_count = int(kill_count)
                if kill_count < 0:
                    print("Please enter a positive integer\n")
                else:
                    break
            else:
                print("Please enter a positive integer\n")

        # simulate kills
        simulate_kills(team_size, kill_count)

        # iterate through and display results
        display_drops()

        # ask if user wants to simulate more kills
        while True:
            again = input("Would you like to simulate more kills? [Y/N]\n")
            if again.lower() == "y":
                # new batch of kills or add to the existing set?
                new_batch = input("Do you want to clear your inventory or build off of it?\n" + 
                "Please type clear if you want to start with a fresh inventory\n")
                if new_batch == "clear":
                    player_inventory.clear()
                break
            elif again.lower() == "n":
                print("Thanks for playing!\n")
                play_again = False
                break;
            else:
                print("Please enter y or n\n")
def welcome():
    print(f"Welcome to the OSRS drop simulator! Here you can simulate boss loot to see how lucky or unlucky you are!\n")

def simulate_kills(team_size, kill_count):
    # simulate kill_count amount of boss kills
    for int in range(kill_count):
        # the drop rate for a unique item at Nex is 1/43
        drop = random.randint(1, NEX_ITEM_DROP_RATE)
        if drop == 43:
            # then the team rolls a number to see who gets a drop
            recipient = random.randint(1, team_size)
            # user is designated as 1, if recipient rolls a 1, the user is getting a unique drop
            if recipient == 1:
                # roll for the item based on weight dict
                decide_drop = str(random.randint(1, 12))
                item = NEX_DROP_TABLE_DICTIONARY.get(decide_drop)
                # add item to user inventory
                player_inventory.append(item)
                print(f"Congrats! You recieved 1x: {item} at {int} kill count!")

def display_drops():
    if len(player_inventory) == 0:
        print("Unlucky! You recieved no unique drops!\n")
    else:
        print("Your inventory: \n")
        for item in player_inventory:
            print(f"You recieved: {item}")

if __name__ == "__main__":
    main()
