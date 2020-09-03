
def undo_redo(strs):
    strs = strs.split()
    indexs = []
    undos = []
    temp = []
    for i in range(len(strs)):

        if strs[i] != 'undo' and strs[i] != 'redo':
            temp.append(strs[i])
        if 'undo' == strs[i] and len(temp) > 0:
            undos.append(temp[-1])
            indexs.append(len(temp)-1)
            temp.pop(-1)
            #print(strs)
        if 'redo' == strs[i]:
            temp.insert(indexs[-1], undos[-1])
            indexs.pop(-1)
            undos.pop(-1)

    return temp

strs = input()
if len(strs) <= 0:
    print()
else:
    strs = strs.replace('\t', ' ')
    results = undo_redo(strs)
    if len(results) == 0:
        print()
    else:
        for i in range(len(results)):
            if i == len(results) -1:
                print(results[i])
            else:
                print(results[i], end=' ')

