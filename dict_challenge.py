loop = True;
while(loop):

    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n")
    marvelchars= {
        "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

        "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"}
            }
    print(f"{char_name}\'s {char_stat} is: {marvelchars[char_name.title()][char_stat.lower()]}")

    user_input = input("Would you like to continue? [Y/N]\n")
    if user_input == 'N' or 'n':
        loop = False;
    else:
        loop = True;
