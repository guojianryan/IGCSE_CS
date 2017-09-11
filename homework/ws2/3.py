"""Modify the program from question 2 so that it now outputs the average of the odd numbers and
also the average of the even numbers."""

numbers = int(input("How many numbers?"))

total_odd = 0
total_even = 0

count_odd = 0
count_even = 0

for count in range(numbers):
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        total_even = total_even + num
        count_even = count_even + 1
    else:
        total_odd = total_odd + num
        count_odd = count_odd + 1

 
print("avg of even numbers:", total_even/count_even)
print("avg of odd numbers:", total_odd/count_odd)