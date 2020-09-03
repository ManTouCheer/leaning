def larger_smaller(a, b):
    if a > b:
        return a, b
    else:
        return b, a
# 欧几里得算法
def Euclid(dividend, divisor):
    origin_dividend, origin_divisor = dividend, divisor
    reminder = dividend % divisor
    while (reminder != 0):
        dividend, divisor = divisor, reminder
        reminder = dividend % divisor

    result = int(origin_dividend * origin_divisor / divisor)
    return result


a, b = map(int, input().split())
dividend, divisor = larger_smaller(a, b)

print(Euclid(dividend, divisor))