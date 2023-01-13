import crayons

# print 'red string in red'
print(crayons.red("red string"))

# red white and blue text
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

# disable the crayons packe
crayons.disable()

# this line should NOT have color because crayons is disabled
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

# enable crayons package again
crayons.DISABLE_COLOR = False

# color has returned
print(f"{crayons.red('red')} white {crayons.blue('blue')}")

# print 'red string' in red
print(crayons.red('red string', bold=True))

# yellow string
print(crayons.yellow('yellow string', bold = True))

# magenta
print(crayons.magenta('magenta string', bold = True))

# white
print(crayons.white('white string', bold = True))
