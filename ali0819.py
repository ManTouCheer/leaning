n = int(input())
lista = list(map(int, input().split()))

results = [0] * n
t = []
for i in range(n):
    tt = [0] * n
    t.append(tt)
t[0] = lista
results[0] = max(lista)
for i in range(1, n):
    index, value = 0, 0
    lenght  = i+1
    times = n-i
    for j in range(times):
        print(t[i-1][j:j+2])
        minv = min(t[i-1][j:j+2])
        print(minv)
        t[i][j] = minv
        print(t)
        if minv > value:
            value = minv
    index = lenght
    results[i] = value

for i in range(n):
    if i != n-1:
        print(results[i], end=' ')
    else:
        print(results[i])






'''
T = int(input())
results = []

for i in range(T):
    n,m = map(int, input().split())
    lista = list(map(int, input().split()))
    listb = list(map(int, input().split()))
    listc = list(map(int, input().split()))
    indexa ,indexb = 0,0
    possible = True
    for c in listc:
        if indexa < n and c == lista[indexa]:
            indexa += 1
        elif indexb < m and c == listb[indexb]:
            indexb += 1
        else:
            results.append('not possible')
            possible = False
            break

    if possible:
        results.append('possible')

for p in results:
    print(p)
'''

