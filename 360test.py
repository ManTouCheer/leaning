n, m = map(int, input().split())
#moperate = map(int, input().split())
moperate = [1] * 0
print(10**5)
n1 = list(range(1, n+1, 2))
n2 = list(range(2, n+1, 2))

def change(n1, n2):
    return n2, n1
def move(n1, n2):
    n1.append(n1[0])
    n1.pop(0)
    return n2, n1

for o in moperate:
    if o == 2:
        n1, n2 = change(n1, n2)
    elif o == 1:
        n1, n2 = move(n1, n2)

for i in range(len(n1)):
    print(n1[i], end=' ')
    if i == len(n1) -1:
        print(n2[i])
    else:
        print(n2[i], end=' ')
'''
n = int(input())

count = 0
isname = True
for i in range(n):
    name = input()
    if len(name)>10:
        continue

    for nn in name:
        #print(nn)
        if not('a' <= nn <= 'z' or 'A' <= nn <= 'Z') :
            isname = False
            #print(name)
            break
    if isname:
        count += 1
    else:
        isname = True
print(count)

'''
'''
5
BA
aOWVXARgUbJDG
OPPCSK_NS
HFD3EEDA
ABBABBBBAA

'''