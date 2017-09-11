"""Factorials don’t work with negative numbers. Amend your program from question 3 to make
sure that only positive numbers (greater than 0) are processed and that the number input is not too
large (you should know this from question 3). The program should check the number which is input
and print a message if it is not acceptable. The program should not attempt to work out the factorial
of any number not within these acceptable limits – think about how you would do this."""

"""
Write a program that allows you to input an integer and outputs the factorial value of that
integer. For example: 4 factorial = 1 x 2 x 3 x4 = 24. Test it.
Try large numbers and see what happens. What is the largest number which works?
"""

MIN = 1
MAX = 10000

number = int(input("Enter a number: "))

if number >= MIN and number <= MAX:
    
    product = 1

    for i in range(1, number + 1):
        product = product * i
    print(product)