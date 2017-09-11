"""Write a program which allows you to input a number and then print out all the multiples of that
number up to 100. Hint: Look at the 3 values used to control a FOR loop. For example:
for x in range( p, q, r):
will start counting at p, count up to q, in steps of r."""

number = int(input("Enter a number:"))

for x in range(0, 101, number):
    print(x)