"""
    print out the first 10 numbers in the sequence, excluding the very first 2. 
"""

num1 = 0
num2 = 1

for count in range(0,10):
   temp = num1
   num1 = num2
   num2 = temp + num1
   print(num2)