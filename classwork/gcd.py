"""
Calculate the Greatest Common Divisor of a and b.
Unless b==0, the result will have the same sign as b (so that when
b is divided by it, the result comes out positive).

This algorithm is invented by Euclidean
"""

a = int(input("Enter a:"))
b = int(input("Enter b:"))

while b != 0:
    temp = b
    b = a%b
    a = temp
    
print(a)