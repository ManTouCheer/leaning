
num_money = 5

def ws(num_monsy):

    if num_money <= 1:
        return 1
    ways = 0
    print(num_money)
    t = int(num_money/2)
    for i in range(t):
        print(t)
        ways += ws(i)
    return ways

print(ws(5))