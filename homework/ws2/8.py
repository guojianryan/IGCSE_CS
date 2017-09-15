"""
Write a program which allows 2 players to play a simple game. Player 1 enters a number
between 1 and 100. Once Player 1 has typed the number and pressed enter, the number should
scroll off the top of the screen, so that Player 2 cannot see it.
You can do that by using a Print statement with lots of Newline codes (\n); for example using:
print(“\n\n\n\n\n\n”) – will print 6 blank lines.
Player 2 now has 7 goes at guessing the number entered by player 1. Each time Player 2 guesses,
check to see if their guess is correct, if not then output a message saying whether their guess is too
high or too low. If player 2 does not guess within 7 turns then player 1 wins.
[Hint: use a for loop to loop for the 7 guesses. In the loop check to see if the number input is
correct, if it is then print a message and then use break to end the loop early]
Does the program work properly? You will find, if you test it thoroughly, that you may well end up
telling winners that they have also lost, why?
"""

number = int(input("Play 1: enter a number:"))

if number >= 0 and number <= 100:
    print("\n" * 50)
    for i in range(7):
        guess = int(input("Play 2: enter a number:"))
        if number > guess:
            print("too low")
        elif number < guess:
            print("too high")
        else:
            print("Congrats!")
            break
    else:
        print("you lost!")
else:
    print("Please enter a number between 0 and 100. ")
