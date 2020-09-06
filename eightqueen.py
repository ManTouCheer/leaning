import numpy as np
import math


def isOK(positions, index):
    if index == 0:
        return True
    if positions[index] in positions[:index]:#不在同一列
        return False
    for i in range(index):
        if positions[i] - i == positions[index] - index: #不在右向斜
            return False
        if positions[i] + i == positions[index] + index: #不在左向斜
            return False
    return True
n = 8
positions = [0]*n
index = 0
ok = False
count = 0
while True:
    #print(positions, index)
    if isOK(positions, index):
        index += 1
    else:
        if positions[index] < n-1:
            positions[index] += 1
        else:
            while positions[index] >= n-1:
                positions[index] = 0
                index -= 1
            if index >= 0:
                positions[index] += 1
            else:
                break
    #print(positions)
    if index == n:
        print(positions)
        index -= 1
        while positions[index] >= n-1:
            positions[index] = 0
            index -= 1
        if index >= 0:
            positions[index] += 1
        else:
            break
        count += 1
print(count)




