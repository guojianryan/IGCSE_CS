ISBN = "9781471809309"

total_odd = 0
total_even = 0

if len(ISBN) != 13:
    print("Invalid ISBN number.")
else:
    for i in range(len(ISBN)):
        if i % 2 == 0:
            total_odd = total_odd + int(ISBN[i])
        else:
            total_even = total_even + int(ISBN[i])
    
    remainder = (3 * total_even + total_odd) % 10
    
    print("valid ISBN" if remainder == 0 else "Invalid ISBN")