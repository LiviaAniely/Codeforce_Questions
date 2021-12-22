n , t = map(int,input().split())

a = list(map(int,input().split()))

i = 1
res = 0

while True:
    
    if i >= t:
        break
    i += a[i -1]


if i == t:
    print('YES')
else:
    print('NO')  