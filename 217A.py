n = int(input())
 
parent = [i for i in range(n + 1)]
tupla = [() for j in range(n + 1)]
 
 
def find(u):
    if u == parent[u]:
        return u
 
    parent[u] = find(parent[u]) 
    return parent[u] 
 
def union(u,v):
    p_u = find(u)
    p_v = find(v)
 
    if p_u != p_v:
        parent[p_v] = p_u      
 
 
for tupl in range(1,n + 1):
    x , y = map(int,input().split())
 
    tupla[tupl] = (x,y)
    
#pegar cada tupla e comparar com as demais 
for i in range(1,n + 1):
   for j in range(1,n + 1):
 
       x1 = tupla[i][0] 
       y1 = tupla[i][1]
 
       x2 = tupla[j][0]
       y2 = tupla[j][1]
 
       if x1 == x2 or y1 == y2:
           union(i,j)
 
 
gp = 0
 
for i in range(1,len(parent)):
    if parent[i] == i:
        gp += 1
 
print(gp - 1)        