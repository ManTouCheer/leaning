from math import sqrt
import timeit


def checkPrimeNumber(n):
    if not isinstance(n, int):
        return False

    else:
        if n == 0 or n == 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

def checkPrimeNumber1(n):
    if not isinstance(n, int):
        return False
    else:
        if n == 0 or n == 1:
            return False
        else:
            for i in range(3,int(n/2) +1, 2):
                if n % i == 0:
                    return False
            return True

def testcheckPrimeNumber(nums):
    for i in nums:
        checkPrimeNumber(i)

def testcheckPrimeNumber1(nums):
    for i in nums:
        checkPrimeNumber1(nums)


if __name__ == '__main__':
    print(timeit.timeit('testcheckPrimeNumber(list(range(1000)))', setup='from __main__ import testcheckPrimeNumber', number=10000))
    #8.811407899999999
    print(timeit.timeit('testcheckPrimeNumber1(list(range(1000)))', setup= 'from __main__ import testcheckPrimeNumber1', number=10000))
    #2.424863

