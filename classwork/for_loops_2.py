"""
Add up all the numbers from 1 to 50
"""

total = 0 #store the result.

for num in range(1, 52):
    total = total + num #
    print("num:", num, "\t total:",total)

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
    print("num =", num, "\t product_even =", product_even, "\t product_odd=", product_odd)

print(product_even)
print(product_odd)

"""
    print the letters in your first name only.
"""

#a usual way
name = "Ryan Guo"
number_of_chars = len(name)

for i in range(0, number_of_chars):
   if name[i] == " ":
       break
   else:
       print(name[i])

#Python's way
for char in name:
   if char == " ":
       break
   else:
       print(char)

# continue
# https://www.tutorialspoint.com/python/python_continue_statement.htm
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter