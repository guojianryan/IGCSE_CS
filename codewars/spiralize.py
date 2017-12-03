#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def spiralize(size):
    if size == 0: return []
    spiral = [[0 for x in range(size)] for y in range(size)]

    left_top = 0
    right_bottom = size - 1

    while left_top <= right_bottom:
        if left_top == right_bottom: 
            spiral[left_top][right_bottom] = 1
            break

        for i in range(left_top, right_bottom+1):#four sides
            spiral[left_top][i] = 1
            spiral[right_bottom][i] = 1
            spiral[i][left_top] = 1
            spiral[i][right_bottom] = 1

        spiral[left_top + 1][left_top] = 0
        if left_top < right_bottom - 3:
            spiral[left_top + 2][left_top + 1] = 1

        left_top += 2
        right_bottom -= 2

    return spiral