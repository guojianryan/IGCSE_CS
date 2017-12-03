#https://www.codewars.com/kata/526d84b98f428f14a60008da
"""Axiom 2: If x is in the sequence, so are 2 * x, 3 * x, and 5 * x."""

def hamming(n):

    i = k = j = 0
    result = [1] 
    for c in range(1, n):
        while result[i] * 2<= result[-1]:
            i += 1
        while result[j] * 3<= result[-1]:
            j += 1
        while result[k] * 5<= result[-1]:
            k += 1

        result.append((min(result[i] * 2, result[j] * 3, result[k] * 5)))

    return result[-1]