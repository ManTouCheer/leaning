
def get_cube_root(d):
    E = 1e-3
    left = 0
    right = d/3
    root = (right - left) / 2 + d
    dev = root ** 3 - d

    while (abs(dev) > E):
        #print(root)
        if dev > 0.0:
            right = root
        else:
            left = root
        root = (right - left)/2 +left
        dev = root ** 3 - d
    return root
p = float(input())
root = get_cube_root(p)
print('{:.1f}'.format(root))