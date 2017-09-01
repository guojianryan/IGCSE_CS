"""
Accept user input and store the value in an integer variable number. 
If number > 0, print “positive”
If number is 0, print “zero”
If number < 0, print “negative”
"""

number = int(input("Enter an integer:"))

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")

if number > 0:
    print("positive")
else:
    if number == 0:
        print("zero")
    else:
        print("negative")   

if number >= 0:
    if number == 0:
        print("zero")
    else:
        print("positive")   
else:
    print("negative")   
