#https://www.codewars.com/kata/5672682212c8ecf83e000050

import bisect

#https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect.bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

def dbl_linear(n):
    seq = [1]
    for i in range(0, n): 
        x2 = seq[0] * 2 + 1
        
        if binary_search(seq, x2) == -1:
            bisect.insort_left(seq, x2)
        
        x3 = seq[0] * 3 + 1
        if binary_search(seq, x3) == -1:
            bisect.insort_left(seq, x3)

        seq.pop(0)

    return seq[0]