ISBN = "978147180930"

total_odd = 0
total_even = 0

if len(ISBN) != 12:
    print("Invalid ISBN number.")
else:
    for i in range(len(ISBN)):
        if i % 2 == 0:
            total_odd = total_odd + int(ISBN[i])
        else:
            total_even = total_even + int(ISBN[i])
                
    temp = (3 * total_even + total_odd) % 10
    
    check_digit = 0 if temp == 0 else 10 - temp
    
    print(check_digit)