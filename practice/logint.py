from math import log10, trunc
from timeit import timeit

##def pow10(n):
##    return 5 ** n << n

def fraction(n):
    return n - trunc(n)

def logint(lo, m=0):
    if lo < 0:
        return 0

    i = 1
    j = pow(10, m+1)
    lo = fraction(lo) + m

    while i + 1 < j:
        u = (i + j) >> 1
        if lo >= log10(u):
            i = u
        else:
            j = u

    if log10(i) <= lo < log10(j):
        return i

    return -1

def test1():
    n = log10(17) * 1922
    k = logint(n, int(n))

def test2():
    n = pow(17, 1922)
##    while n > 1e2:
##        n //= 10

number = 1000

print(timeit(test1, number=number), timeit(test2, number=number))