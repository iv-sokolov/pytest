from random import randint
n = randint(1, 1000)
if n <= 223:
    m = randint(1, n**2)
else: m = randint(1, 50000)
x = 0
y = 0
f=open('input.txt', 'w')
print(str(n) + ' ' + str(m), file=f)
for i in range(m):
    x = randint(1, n)
    y = randint(1, n)
    z=(str(x)+' '+str(y))
    print(z, file=f)
f.close()
