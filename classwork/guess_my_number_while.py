"""Guess my number game, give the player as many times as they need"""

from random import randrange
my_number = randrange(1,10)

while True: # keep running, untils it breaks. 
    guess = int(input("enter a number:"))

    if guess == my_number:
        print("Hooray!")
        break
    else:
        print("Try again!")