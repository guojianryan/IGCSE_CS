"""
Write a program that allows you to input an integer and outputs the factorial value of that
integer. For example: 4 factorial = 1 x 2 x 3 x4 = 24. Test it.
Try large numbers and see what happens. What is the largest number which works?
"""

number = int(input("Enter a number: "))

product = 1

for i in range(1, number + 1):
    product = product * i

print(product)

