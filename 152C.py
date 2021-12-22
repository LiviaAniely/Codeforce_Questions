n,m = map(int,input().split())

palavras = []
for i in range(n):
    palavras.append(input())

resp = 1

for i in range(m):
    visitados = set()
    for p in palavras:
        visitados.add(p[i])

    resp *= (len(visitados) % 1000000007 )


print(resp % 1000000007)