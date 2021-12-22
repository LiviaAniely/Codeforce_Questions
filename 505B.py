import sys
sys.setrecursionlimit(100000)

n,m = map(int,input().split())

las = [[[] for i in range(n + 2)] for j in range(101)]
visitados = [[False for i in range(n + 2)] for j in range(101)]


for i in range(m):
    v1,v2,cor = map(int,input().split())

    las[cor][v1].append(v2)
    las[cor][v2].append(v1)


def dfs(x,i):
    visitados[i][x] = True

    for elem in las[i][x]:
        if not visitados[i][elem]:
            dfs(elem,i)

queries = int(input())

for q in range(queries):
    inicio,fim = map(int,input().split())

    soma = 0
    for i in range(101):
        dfs(inicio,i)

        if visitados[i][fim]:
            soma += 1
    
    visitados = [[False for i in range(n + 2)] for j in range(101)]
    print(soma)