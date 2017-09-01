from random import randrange
my_number = randrange(1,10)

for i in range(1, 6):
    guess = int(input("enter a number:"))

    if guess == my_number:
        print("Hooray!")
        break
    else:
        print("Try again!")