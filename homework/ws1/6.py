"""Write a program which will input 2 decimal numbers. The program should check to see if the
smaller number is a factor of the larger number. Your program should take the numbers in any
order, largest first or smallest first, and still give the correct answer."""

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num2 > num1:
    num2, num1 = num1, num2

if num2 != 0 and num1 % num2 != 0:
    print("No")
else:
    print("Yes")