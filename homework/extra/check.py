#parameters: the positions of queen and king, both are numbers from 0 - 7   
def queen_check(queen, king):
    return queen[0] == king[0] \
        or queen[1] == king[1] \
        or queen[0] - queen[1] == king[0] - king[1] \
        or queen[0] + queen[1] == king[0] + king[1] 

print(queen_check([1,2],[3,1]))