# -*- coding: UTF-8 -*-

from math import trunc
import time

log10_2 = 0.3010299956639812

log10_digits = [
    0.0,
    0.3010299956639812,
    0.4771212547196624,
    0.6020599913279624,
    0.6989700043360189,
    0.7781512503836436,
    0.8450980400142568,
    0.9030899869919435,
    0.9542425094393249,
    1.0,
]

##def taylor10(x):
##    assert 0 <= x <= 1, x
##
##    px = x
##    r = 1
##    coes = (
##        2.302585092994046,
##        2.6509490552391997,
##        2.034678592293477,
##        1.1712551489122673,
##        0.5393829291955817,
##        0.2069958486968682,
##    )
##
##    for coe in coes:
##        r += coe * px
##        px *= x
##
##    return r

def search_contigous_interval(intervals, x):
    i = 0
    j = len(intervals) - 1

    while i + 1 < j:
        u = (i + j) >> 1
        if x >= intervals[u]:
            i = u
        else:
            j = u

    if intervals[i] <= x < intervals[j]:
        return i

# n = log_10(2 ** u) 에 대하여 2 ** u 의 최상위 숫자를 구합니다.
def powbit(n):
    return 1 + search_contigous_interval(log10_digits, n - trunc(n))

def banford(mass, n):
    u = 0
    for i in range(n):
        b = powbit(u)
        u += log10_2
        mass[b] += 1

    return mass

def transform(src):
    tot = sum(src)
    return [elem / tot for elem in src]

def main():
    n = 10000
    t = time.time()
    mass = banford([0 for i in range(10)], n)
    mass = transform(mass)

    print(time.time() - t)
    print(mass)

if __name__ == '__main__':
    main()
