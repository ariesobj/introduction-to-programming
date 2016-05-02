from math import trunc

def binary(w, an):
    # assumption... how can we break this assumption? do we impl sort algorithm?
    # do we change search algorithm?
    an.sort()

    i = 0
    j = len(an) - 1
    while i <= j:
        m = (i + j) // 2
        if an[m] > w:
            j = m - 1
        elif an[m] < w:
            i = m + 1
        else:
            return m

    return -1

def gcd(x, y):
    while x % y > 0:
        x, y = y, x % y
    return y
