import decimal
import numpy
n, m = map(int, input().split())

_t = []
_t.append([-1] * (n+2))
for i in range(n):
    _d = list(map(int, input().split()))
    _d = [-1] + _d + [-1]
    _t.append(_d)
_t.append([-1] * (n+2))
juzhen  = numpy.array(_t)

for i in range(1, n+1):
    for j in range(1, m+1):
        mmm = 1
        a1 = int(juzhen[i-1][j])
        a2 = int(juzhen[i+1][j])
        a3 = int(juzhen[i][j-1])
        a4 = int(juzhen[i][j+1])
        me = int(juzhen[i][j])
        print(juzhen)
        mmm = mmm+1 if a1 > -1 else mmm
        mmm = mmm + 1 if a2 > -1 else mmm
        mmm = mmm + 1 if a3 > -1 else mmm
        mmm = mmm + 1 if a4 > -1 else mmm
        sumn = me
        sumn = sumn + a1 if a1 > -1 else sumn
        sumn = sumn + a2 if a2 > -1 else sumn
        sumn = sumn + a3 if a3 > -1 else sumn
        sumn = sumn + a4 if a4 > -1 else sumn
        print(sumn, mmm)
        ave = decimal.Decimal(str(sumn))/ decimal.Decimal(str(mmm))
        print(ave)
        if int(ave*10)% 10 > 5:
            ave += 1
        juzhen[i][j] = int(ave)


for i in range(1, n+1):
    for j in range(1, m+1):
        print(juzhen[i,j], end= ' ')
    print()