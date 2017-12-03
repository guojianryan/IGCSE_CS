#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(array):
    result = []
    if len((array[0])) == 0: 
        return result
    row, col = 0, 0
    start, end = 0, len(array) - 1
    direction = 0 # 0 right, 1 down, 2 left, 3 up
    for i in range(len(array) ** 2):
        result.append(array[row][col])

        if direction == 0:
            col = col + 1
            if col == end:
                direction = 1
        elif direction == 1:
            row = row + 1
            if row == end:
                direction = 2
        elif direction == 2:
            col = col -1
            if col == start:
                direction = 3
        elif direction == 3:
            row = row - 1
            if row == start + 1:
                direction = 0
                end = end - 1
                start = start + 1
    return result