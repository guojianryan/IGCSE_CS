"""
Ask the user to enter “hello”. 
If another word is entered, ask again. 
"""

while True:
    n = input("Please enter 'hello':")
    if n.strip() == 'hello':
        break