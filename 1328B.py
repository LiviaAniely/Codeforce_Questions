t = int(input())

for teste in range(t):
    n, k = map(int,input().split())

    s = ["a" for j in range(n)]

    for i in range(n-1,-1,-1):
        if k <= n - i - 1:
            s[i] = "b"
            s[n - k] = "b"
            
            for letra in s:
                print(letra,end = "")
            print()
            break
        
        k-= n - i - 1