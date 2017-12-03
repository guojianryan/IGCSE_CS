#https://www.codewars.com/kata/54b72c16cd7f5154e9000457

from collections import defaultdict

def trailing_zeros(num, base):
    base_primes = primes(base)
    base_keys = base_primes.keys()
    num_primes = dict.fromkeys(base_keys, 0)
   
    for key in base_keys:
        now = key
        while now <= num:
           num_primes[key] =  num_primes[key] + num // now
           now = now * key

    mul = [(num_primes[key])//(base_primes[key]) for key in base_keys]

    return min(mul)


def primes(n):
    primfac = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            primfac[d] =  primfac[d] + 1
            n = n / d
        d = d + 1

    if n > 1:
        primfac[n] = 1
    
    return dict(primfac)

print(trailing_zeros(314159265358, 2718))

