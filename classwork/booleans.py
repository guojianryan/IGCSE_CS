"""
Booleans and comparisons
"""

comp = 2 > 1 # True as 2 is greater 1

"""
The function "input" asks the user to answer a quetion. The result is a string. 
The function "int" converts the string to an integer.
"""
age = int(input("How old are you?"))

is_adult = age >= 18 
print(is_adult)

is_new_born = age == 0
print(is_new_born)

gender = input("What is your gender?")

is_not_girl = gender != "F"
print(is_not_girl)

"""
Assignments and "is equal to"
"""

times = 1 # single equal sign ==> assignment

"""
    times == 1 is evaluated first ==> True
    set is_time_1 to True
"""
is_times_1 = times == 1 # double equal signs ==> is equal to
print(is_times_1)

"""
and, or and not
"""

sat = True
sun = False
weekend = sat or sun #if it is Saturday or Sunday
print(weekend)

weekday = not weekend
print(weekday)

working_hours = False
working = weekday and working_hours 

print(working)
