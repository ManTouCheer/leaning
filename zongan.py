a = [1, -2, 3, 5 ,-2, 6, -1]

_list = [0]
ei = 0
si = 0
MAX = 0
for i in range(len(a)):
    maxx = 0
    _si =0
    for j in range(len(_list)):
        _list[j] = a[i] + _list[j]
        if maxx < _list[j]:
            maxx = _list[j]
            _si = j
    _list.append(0)
    if _si == si:
        if MAX < maxx:
            ei = i
    else:
        si = _si
print(a[si:ei])

