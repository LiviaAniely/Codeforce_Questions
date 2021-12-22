from math import factorial

def comb2(n):
    if n >= 2:
        comb = factorial(n) / (2 * factorial(n - 2))
        return comb
    else:
        return 0

n = int(input())

freq = [0 for i in range(26)]

for i in range(n):
    palavra = input()

    ind = ord(palavra[0]) - ord("a")
    freq[ind] += 1

resp = 0

for elem in freq:
    if elem > 1:
        sala1 = elem // 2
        sala2 = elem - sala1
        resp += comb2(sala1)
        resp += comb2(sala2)


print(int(resp))
