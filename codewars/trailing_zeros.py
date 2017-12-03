from collections import defaultdict

def trailing_zeros(num, base):
    base_primes = primes(base)
    base_keys = base_primes.keys()
    num_primes = dict.fromkeys(base_keys, 0)
    zeros = 0 
    for count in xrange(num, 0, -1):
        for key in base_keys:
            while count % key == 0:
                num_primes[key] =  num_primes[key] + 1
                count = count / key

    print("the end of num primes")
    
    multiples = []
    for k, v in num_primes.items():
        multiples.append(v / base_primes[k])

    zeros = int(min(multiples))

    return zeros


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

#print(trailing_zeros(1024, 2))

print(trailing_zeros(314159265358, 2718))

