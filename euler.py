k,  n = input().split(' ')
k = int(k)
n = int(n)
import math
'''
Следующая конструкция сокращает дробь:
'''

if n - k <= k:
    p = k + 1 #первый множитель числителя
    q = n - k #последний множитель знаменателя
else:
    p = n - k + 1 #первый множитель числителя
    q = k #последний множитель знаменателя

'''
Следующая конструкция строит
необходимый список простых чисел:
'''
is_prime = list()
primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
    151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
    311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
    479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
    577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
    659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751,
    757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853,
    857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
    953, 967, 971, 977, 983, 991, 997
    ]
if n >= 1000:
    is_prime = list()
    limit = n + 1
    sqlimit=int(math.sqrt(limit))
    is_prime = [False] * (limit + 1)
    for x in range(1, sqlimit+1):
        z = x*x
        for y in range(1, sqlimit+1):
            c = 4 * z + y * y
            if c <= limit and (c % 12 == 1 or c % 12 == 5):
                is_prime[c] = not is_prime[c]
                c = 3 * z + y * y
                if c <= limit and c % 12 == 7:
                    is_prime[c] = not is_prime[c]
                    c = 3 * z - y * y
                    if x>y and c <= limit and c %12 == 11:
                        is_prime[c] = not is_prime[c]
    for c in range(5, sqlimit):
        if is_prime[c]:
            for d in range(c**2,limit+1,c**2):
                is_prime[d] = False

    for c in range(998,limit):
        if is_prime[c]: primes.append(c)
else:
    pass
primes=tuple(primes)
'''
Объявляем числитель и знаменатель:
'''

num= []
den = []

'''
Факторизуем числитель:
'''

for i in range(p, n+1):
    s = i
    if s in primes:
        num.append(s)      
        continue
    else:
        for j in primes:
            a = j
            if (a <= s and s % a == 0):
                while (a <= s and s % a == 0):                      
                    s //= a
                    num.append(a)
            elif (a < s and s % a != 0):
                continue
            else:
                break
numd = dict.fromkeys(set(num), 0)
for key in numd.keys():
    temp_key=key
    for i in num:
        if i == temp_key:
            numd[temp_key] += 1
'''
Факторизуем знаменатель:
'''

for i in range(1, q+1):
    t=i
    if t in primes:
        den.append(t)
        continue
    else:
        for j in primes:
            b = j
            if (b <= t and t % b == 0):
                while b <= t:
                    t //= b
                    den.append(b)
                    if  t % b == 0:
                        continue
                    else:
                        break
            elif (b < t and t % b != 0):
                continue
            else:
                break

dend = dict.fromkeys(set(den), 0)
for key in dend.keys():
    temp_key=key
    for i in den:
        if i == temp_key:
            dend[temp_key] += 1

'''
Сокращаем дробь, вычеркивая совпадающие
простые делители числителя и знаменателя:
'''

for key in dend.keys():
    if key in numd.keys():
        numd[key] -= dend[key]
        
res = {}
for key in numd.keys():
    temp_key=key
    if numd[temp_key] != 0:
        res[temp_key] = numd[temp_key]
'''
Вычисляем функцию Эйлера по известному
разложению числа на простые:
'''

euler = 1
for key in res.keys():
    euler *= key ** res[key] - key ** (res[key] - 1)
    euler %= 1000000007
    
print(euler)
