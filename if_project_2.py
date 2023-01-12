#!/usr/bin/env python3

#introduction
print("Should you learn Python, Java, or Javascript?\n")

# if the user wants low complexity, point them towards python
syntax = input("What level of syntax complexity do you want? \n Enter \'Low\' or \'Moderate\'\n")

# valid user input so that they can only enter 'low' or 'moderate'
while True:
    if syntax.lower() == 'low' or syntax.lower() == 'moderate':
        break
    else:
        syntax = input("What level of syntax complexity do you want? \n Enter \'Low\' or \'Moderate\'\n")


if syntax.lower() == 'low':
    # if they absolutely need ++ and --, point them elsewhere
    operator = input("Do you need the ++ and -- operators?\nPlease enter Yes or No \n")
    while True:
        if operator.lower() == 'yes' or operator.lower() == 'no':
            break
        else:
            operator = input("Do you need the ++ and -- operators?\nPlease enter Yes or No \n")
    if operator.lower() == 'no':
        print("I think Python would be a great programming language for you to learn!")
    else:
        print("Python has no ++ or -- operator. Try Java or Javascript!")
else:
    # if they are interested in web design, suggest Javascript
    web_design = input("Are you looking to build a website or get into web design?\n Enter Yes or No \n")
    while True:
        if web_design.lower() == 'yes' or web_design.lower() == 'no':
            break;
        else:
            web_design = input("Are you looking to build a website or get into web design?\n Enter Yes or No \n")
    if web_design.lower() == 'no':
        print("You chose moderate syntax complexity and no interest in web design, I recommend learning Java!")
    else:
        print("You chose moderate syntax complexity with an interest in web design, I recommend learning Javascript!")
