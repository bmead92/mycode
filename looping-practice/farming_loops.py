#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
                      {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# loop through and return the animals in the NE Farm

print(farms[0]['agriculture'])

# have the user choose which farm they want to few the agriculture of
for farm in farms:
    print("-", farm["name"])
choice = input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        print(farm["name"]["agriculture"])
