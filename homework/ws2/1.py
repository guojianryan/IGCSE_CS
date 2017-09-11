"""Write a program to allow you to input 10 numbers. The program should count how many odd
numbers are in the list and how many even numbers. It should print the totals at the end. Use a for
loop for this. The technique for checking odd or even was covered in the previous worksheet."""

total = 0

for count in range(10):
    total = total + float(input("Enter a number:"))

print(total)