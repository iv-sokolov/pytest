k,  n = input().split(' ')
k = int(k)
n = int(n)
import math
is_prime = list()
limit = n + 1
sqlimit=int(math.sqrt(limit))
is_prime = [False] * (limit + 1)
for x in range(1, sqlimit+1):
    z = x ** 2
    for y in range(1, sqlimit+1):
        c = 4 * z + y ** 2
        if c <= limit and (c % 12 == 1 or c % 12 == 5):
            is_prime[c] = not is_prime[c]
        c = 3 * z + y ** 2
        if c <= limit and c % 12 == 7:
            is_prime[c] = not is_prime[c]
        c = 3 * z - y ** 2
        if x>y and c <= limit and c %12 == 11:
            is_prime[c] = not is_prime[c]
for c in range(5, sqlimit):
    if is_prime[c]:
        for d in range(c**2,limit+1,c**2):
            is_prime[d] = False
primes=[]
primes.append(2)
primes.append(3)
for c in range(5,limit):
    if is_prime[c]: primes.append(c)
primes=tuple(primes)
