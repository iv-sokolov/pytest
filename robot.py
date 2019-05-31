n = int(input())
x = 0
y = 0
k=0
t=1
while n > 2*t:
    k += 1
    n -= 2*k
    x += k*((-1)**k)
    y += k*((-1)**k)
    t=k
if (n <= k+1):
    if k % 2 == 0:
        x = x - n
        y = y
    else:
        x = x + n
        y = y
else:
    if k % 2 == 0:
        x = x - k
        y = y - (n - k)
    else:
        x = x + k
        y = y + (n - k)
print(str(x) + ' ' + str(y))
