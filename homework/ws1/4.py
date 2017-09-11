"""
Write a short program to allow the user to input the weather conditions: Cold, Cloudy, Hot.
Depending on which they input your program should output a short sentence advising them to:
 Wear a coat
 Take an umbrella
 Wear sun cream
"""

weather = input("How is the weather:")

if weather == "Cold":
    print("Wear a coat")
elif weather == "Cloudy":
    print("Take an umbrella")
elif weather == "Hot":
    print("Wear sun cream")
else:
    print("invalid data input")

