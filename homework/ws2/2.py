"""Convert the program in question 1 so that it no longer works only with 10 numbers, but works by
using the first number input to tell the computer how many numbers will follow. For example, the
sequence: 4, 34, 23, 82, 19 works like this: input 4 – which says that 4 numbers will follow, those 4
numbers are 34, 23, 82, 19."""

numbers = int(input("How many numbers?"))

total = 0

for count in range(numbers):
    total = total + float(input("Enter a number:"))
 
print(total)