"""
string operations
"""

# Plus sign(+) for concatenation
first_name = "Tom"
last_name = "Cruise"
full_name = first_name + " " + last_name

print(full_name)

"""
last_name is a string object. upper() is a method of String class.
With the dot notation, you  tell the program to change the each letter in the string to upper case. 
"""
full_name_2 = first_name + " " + last_name.upper()

print(full_name_2)

length = len(full_name_2)

print("The length of the string is", length, ".")