"""Write a short computer program to allow a person to input their name and then their gender.
The program should then output their name with Mr or Miss in front of ."""

name = input("your name:")

gender = input("your gender(F/M):")

if gender == "F":
    print("Miss", name) #same as print("Miss" + " " + name)
elif gender == "M":
    print("Mr", name)
else:
    print("invalid data input")