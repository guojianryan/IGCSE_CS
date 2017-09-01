"""
Swapping numbers
"""

# with an extra variable

x = 100
y = 200

temp = x
x = y
y = temp

print(x)
print(y)

# no extra variable, but might overflow
x = 100 
y = 200

x = x + y
y = x - y
x = x - y

print(x)
print(y)

# no extra variable. 
# bitwise operator used

x = 100
y = 200

x = x ^ y
y = x ^ y
x = x ^ y

print(x)
print(y)