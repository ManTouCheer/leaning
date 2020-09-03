import numpy as np
k = int(input())
scores = 0
listb0 = []
listb1 = []
for i in range(k):
    a, b = map(int, input().split())
    if b == 0:
        listb0.append(a)
    else:
        listb1.append(a)
npb0 = np.array(sorted(listb0, reverse=True))
npb1 = np.array(sorted(listb1, reverse=True))

score0 = sum(npb0)
indexnpb1 = 0
for i in range(len(npb1)):
    if score0 < npb1[i]:
        score0 += npb1[i]
    else:
        indexnpb1 = i
        break
#print(score0)
#print(len(npb1[indexnpb1: ]))
score1 = 2**(len(npb1[indexnpb1:]))
scores = score0 * score1
print(scores)



'''
sameLetters = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']

while True:
    _str = input()
    if len(_str)<=0:
        break
    half = len(_str) // 2 +1
    lenght = len(_str)

    #print(half, lenght)
    isYes = True
    for i in range(half):
        if not (_str[i] == _str[lenght - i-1] and _str[i] in sameLetters):
            isYes = False
            break
    if isYes:
        print("YES")
    else:
        print("NO")
'''