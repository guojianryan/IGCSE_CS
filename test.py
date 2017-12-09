def palindrome(str):
    length = len(str)
    for index in range(0, length // 2):
        if str[index] != str[length-index-1]:
            return False
    return True

def reverse(array):
    size = len(array)
    for index in range(0, int(size / 2)):
        temp = array[index]
        array[index] = array[size - index - 1]
        array[size - index - 1] = temp
    return array

def is_prime(n):
    for num in range(2, int(n/2)):
        if n % num == 0:
            return False
    return True

def gcd(x, y):
    while y != 0:
        temp = x
        x = y
        y = temp % y
    return x
