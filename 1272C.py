n, k = map(int,input().split())

sequencia = list(input())

letras_funcionam = list(input().split())

for i in range(len(sequencia)):
    if sequencia[i] in letras_funcionam:
        sequencia[i] = 1
    else:
        sequencia[i] = 0

j = 0
resp = 0
i = 0
while j < len(sequencia):
    if sequencia[j] == 1:
        j += 1
    else:
        resp += ((j - i) * (j - i + 1)) / 2
        i = j + 1
        j += 1

if sequencia[-1] == 1:
    resp += ((j - i) * (j - i + 1)) / 2
    
print(int(resp))
