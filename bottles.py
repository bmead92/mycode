#!/usr/bin/env python3

# print 99 bottles of beer on the wall song

def bottles(num):
    for bottle in range(num, 1, -1):
        print(f"{num} bottles of beer on the wall!")
        print(f"{num} bottles of beer on the wall! {num} bottles of beer! You take one down, pass it around")
        num -= 1
def main():
    while True:
        how_many = input("How many bottles of beer are on the wall?\n type Q to quit at any time")
        if how_many.lower() == 'q':
            break
        elif int(how_many.isdigit()) and int(how_many) < 100:
            bottles(int(how_many))
            break
        else: print("Please enter a number below 100")
if __name__ == '__main__':
    main()
