n,s=map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

#entrar
path = False
if a[0] != 0:

    #ir diretamente
    if a[s - 1] == 1:
        path = True
    else:
        #trocar de metro

        for i in range(s,n):
            if a[i] == 1 and b[i] == 1:
                if b[s - 1] == 1:
                    path = True
                    break


if path:
    print("YES")
else:
    print("NO")    
