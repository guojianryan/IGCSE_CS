"""
You've finished eating at a restaurant, and received this bill:
Cost of meal: $44.50
Restaurant tax: 6.75%
Tip: 15%
You'll apply the tip to the overall cost of the meal (including tax).
Calculate the total cost of the meal and print the result.
"""

cost= 44.5
tax = .0675
tip = .15

total = cost * (1 + tax) * (1 + tip)

print(total)

#extension, round to 2 decimal places

print(round(total,2))