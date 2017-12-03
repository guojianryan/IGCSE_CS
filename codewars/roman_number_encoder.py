#https://www.codewars.com/kata/51b62bf6a9c58071c600001b

def solution(n):
    
    thousands = n//1000
    hundreds = (n - 1000 * thousands) // 100
    tens = (n - 1000 * thousands - hundreds * 100) // 10
    ones = (n - 1000 * thousands - hundreds * 100 - tens * 10) 
    
    result = "M" * thousands
    
    if hundreds == 9:
        result += "CM"
    elif hundreds >= 5: 
        result += "D" + "C" * (hundreds - 5)
    elif hundreds > 2:
        result += "C" * (5 - hundreds) + "D"
    elif hundreds > 0:
        result += "C" * hundreds
        
    if tens == 9:
        result += "XC"
    elif tens >= 5: 
        result += "L" + "X" * (tens - 5)
    elif tens > 2:
        result += "X" * (5 - tens) + "L"
    elif tens > 0:
        result = "X" * tens
        
    if ones == 9:
        result += "IX"
    elif ones >= 5: 
        result += "V" + "I" * (ones - 5)
    elif ones > 2:
        result += "I" * (5 - ones) + "V"
    elif ones >0:
        result += "I" * ones

        
    return result