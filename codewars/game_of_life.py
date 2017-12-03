#https://www.codewars.com/kata/52423db9add6f6fc39000354

#Not an elegant solution, but does the job.

import copy

def get_generation(cells, generations):

    if generations == 0: 
        return cells
    else:
        cc = copy.deepcopy(cells)
        c = copy.deepcopy(pad_matrix(cc))
        rows = len(cc)
        cols = len(cc[0])
        for row in range(rows):
            for col in range(cols):
                alive = get_number_alive(cc, rows, cols, row, col)
                if cc[row][col] == 1:
                    if alive not in [2, 3]:
                        c[row][col] = 0
                else:
                    if alive == 3:
                        c[row][col] = 1
        return get_generation(remove_zero_padding(c), generations - 1)

def get_number_alive(cells, rows, cols, row, col):
    alive = 0
    test_alive = lambda row, col: cells[row][col]==1
    if row != 0:
        alive += 1 if test_alive(row - 1, col) else 0 #top
        if col != 0:
            alive += 1 if test_alive(row - 1, col - 1) else 0 # top left
        if col != cols - 1:
            alive += 1 if test_alive(row - 1, col + 1) else 0 # top right
    
    if col != 0:
            alive += 1 if test_alive(row, col - 1)==1 else 0 #  left
    if col != cols - 1:
            alive += 1 if test_alive(row, col + 1)==1 else 0 #  right

    if row != rows - 1:
        alive += 1 if test_alive(row + 1, col)==1 else 0 #bottom
        if col != 0:
            alive += 1 if test_alive(row + 1, col - 1)==1 else 0 # bottom left
        if col != cols - 1:
            alive += 1 if test_alive(row + 1, col + 1)==1 else 0 # bottom right
    return alive

def pad_matrix(cells):
    cols = len(cells[0])
    cells.insert(0, [0] * cols)
    cells.append([0] * cols)
    
    for i in range(len(cells)):
        cells[i].insert(0,0)
        cells[i].append(0)

    return cells

def remove_zero_padding_by_rows(cells):
    zeros = set([0] * len(cells[0]))

    index = len(cells) - 1
    while index >= 0:
        if len(set(cells[index]) - zeros) == 0:
            del cells[index]
            index -= 1
        else:
            break

    index = 0
    while index < len(cells) - 1:
        if len(set(cells[index]) - zeros) == 0:
            del cells[index]
        else:
            break

    return cells

def remove_zero_padding(cells):
    c = remove_zero_padding_by_rows(cells)
    c = [list(x) for x in list(zip(*c))]
    c = remove_zero_padding_by_rows(c)
    c = [list(x) for x in list(zip(*c))]
    return c