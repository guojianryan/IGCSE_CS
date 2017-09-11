"""Write a program to allow the user to input 2 decimal numbers. The program should treat these
as lengths of a rectangle and output their area.

Now modify the program so that after the lengths have been input the user also needs to input a T
or a R, so say whether they are lengths of a triangle or rectangle. The program should output the
correct area accordingly."""


len_or_base = float(input("Enter the first number:"))
witdh_or_height = float(input("Enter the second number:"))

shape = input("T or R?")

if shape == "T":
    print(len_or_base * witdh_or_height /2)
elif shape == "R":
    print(len_or_base * witdh_or_height)
else:
    print("Please enter T or R only")