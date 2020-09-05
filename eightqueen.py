import numpy as np
import math

checkerboard = np.zeros(shape=(8,8), dtype = np.int)

queen_pos= {}

def isOK(positions, index):
    if positions[index] in positions[:index-1]:#不在同一列
        return False
    for i in range(index):
        if positions[i] - i == positions[-1] - index: #不在右向斜
            return False
        if positions[i] + i == positions[-1] + index: #不在左向斜
            return False
    return True

