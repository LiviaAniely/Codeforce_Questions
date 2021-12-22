n , m = map(int,input().split())
 
visitado = [False for i in range(100000)]
 
import queue
def bfs(x,fim):
    visitado[x] = True
    q = queue.Queue()
    q.put((x*2,x - 1,1))

    while not visitado[fim] == True:
        node = q.get()

        for i in node[:2]:
 
            if visitado[i] == False:
                visitado[i] = True
                if i != fim:
                    if i * 2 <= 20000 and i - 1 >= 0 :
                        q.put((i * 2,i - 1,node[2] + 1))
 
                
    return node[2]  
print(bfs(n,m))  