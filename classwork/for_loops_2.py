"""
Add up all the numbers from 1 to 50
"""

total = 0 #store the result.

for num in range(1, 52):
    total = total + num #

print(total)

# second way
total = 52 * 51 / 2 # simple math, more effecient
print(total)


"""
Find the answer of 2 * 4 * 6 * 8 * 10…. * 28 and 1 * 3 * 5 * 7 ….. 27 in a loop
"""
product_even = 1
product_odd = 1

for num in range(1, 29):
    if num % 2 == 0:
        product_even = product_even * num
    else:
        product_odd = product_odd * num

print(product_even)
print(product_odd)


"""
    print the letters in your first name only.
"""
for char in "Ryan Guo":
   if char == " ":
       break
   else:
       print(char)


