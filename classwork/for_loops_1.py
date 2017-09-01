"""
print 1 - 3
"""

#without a loop

#the first iteration
i = 1
print(i)

#the second iteration
i = i + 1
print(i)

#the third iteration
i = i + 1
print (i)

#imagin you are going to the the same task 100 times. 

# a loop which does the same job
for i in range(1, 4): 
    print(i)

# 1 - 100
for i in range(1, 101): # default step size
    print(i)

#print out the the odd numbers from 1 - 100
for i in range(1, 101, 2): # the last parameter is the step size
    print(i)

for i in range(1, 100):
    if i % 2 != 0:
        print(i)

