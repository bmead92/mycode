#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    # print the moves and display
    print(pokeapi["sprites"]["front_default"])
    for move in pokeapi["moves"]:
        print(move["move"]["name"])

    # print the game_indicies
    # count total number of games
    # display results
    game_count = 0
    for game in pokeapi["game_indices"]:
        game_count += 1
    print(f"{pokeapi['forms'][0]['name']} has appeared in {game_count} games")
main()

