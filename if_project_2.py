#!/usr/bin/env python3

#introduction
print("What programming language you should learn?\nAnswer the next few questions to find out!\n")

#question 1
syntax = ''
while syntax.lower() != "low" or "moderate":
    syntax = input("What level of syntax complexity do you want? \n Enter \'Low\' or \'Moderate\'\n")
if syntax.lower() == 'low':
    #question 3
    operator = input("Do you absolutely love the ++ operator and have to have it?\n Please enter Yes or No \n")
    if operator.lower() == 'no':
        print("I think Python would be a great programming language for you to learn!")
    else:
        print("Python has no ++ or -- operator, and you stated that these are a must. Try Java or Javascript!")
else:
    #question 2
    web_design = input("Are you looking to build a website or get into web design?\n Enter Yes or No \n")
    if web_design.lower() == 'no':
        print("You chose moderate syntax complexity and no interested in web design, I recommend learning Java!")
    else:
        print("You chose moderate syntax complexity with an interest in web design, I recommend learning Javascript!")
