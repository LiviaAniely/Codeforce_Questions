r , c = map(int,input().split())
#r=linhas,c=colunas

matriz_de_adjacencia = []

for i in range(r):
    matriz_de_adjacencia.append(list(input()))
w = False
s = False

#Casos
for i in range(r):
    for j in range(c):

        if matriz_de_adjacencia[i][j] == 'S':
            s = True

            if i - 1 >= 0 : #acima de S
                if matriz_de_adjacencia[i - 1][j] == 'W': 
                    w = True

            if i + 1  <= r - 1: #abaixo de S 
                if matriz_de_adjacencia[i + 1][j] == 'W':
                    w = True

            if  j + 1 <= c - 1: #à direita de S
                if matriz_de_adjacencia[i][j + 1] == 'W':
                    w = True

            if j - 1 >= 0 : #à esquerda de S
                if matriz_de_adjacencia[i][j - 1] == 'W':
                    w = True  


if w: #se tem w junto de s
    print('No')  

else:

    for linha in range(r):
        for coluna in range(c):

            if matriz_de_adjacencia[linha][coluna] == '.':
                matriz_de_adjacencia[linha][coluna] = 'D'

    print('Yes')

    for l in range(r):
        for co in range(c):
            
            print(matriz_de_adjacencia[l][co],end = '')
        print()