"""
print 1 - 3
"""

#for loop
for i in range(1, 4): #i is increased by 1 each iteration
    print(i)

#while loop
count = 1
while count < 4:
    print(count)
    count = count + 1 #count is increaed by 1 each iteration, but the programmer has to do it. 


"""
print out the the odd numbers from 1 - 100
"""

#for loop
for i in range(1, 101, 2): # the last parameter is the step size
    print(i)

#while loop
count = 1
while count < 101:
    print(count)
    count = count + 2 # step size: 2. program responsibility to increase count by 2


"""
    print the letters in your first name only.
"""

#for loop
for char in "Ryan Guo":
   if char == " ":
       break
   else:
       print(char)

#while loop
index = 0
name = "Ryan Guo"
while index < len(name):
    index = index + 1
    if char == " ":
        break
    else:
        print(char)