n , m = map(int,input().split())

la = [] #lista onde ficará o caminho inverso
y = m
#fazer o caminho inverso,indo de m --> n, verificando se é possível chegar em n a partir de m
while True:
    if y % 2 == 0:
        la.append(y // 2)
        y = int(y / 2)

    elif (y - 1) % 10 == 0:
        la.append((y - 1) // 10)  
        y = int((y -1) / 10) 
    else:
        break    
    if y < n:
        break

if n not in la:
    print('NO')
else:
    #verificar se há algum elemento além do próprio n,se True,quer dizer que o último elemento é menor que n
    if len(la) > 1:
        la.pop(-1)

    la = sorted(la) 

    print('YES')

    if la[0] != n:
        print(len(la) + 2)
        print(n,end = ' ')
    else:
        print(len(la) + 1) 

    for i in la:
        print(i,end = ' ')  
          
    print(m)    