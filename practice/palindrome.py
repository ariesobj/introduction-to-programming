# 구현하기 귀찮음
from math import floor, ceil

# 정수 집합에서 정의된 자기 자신을 제외한 최소 하계
U = lambda x: floor(x + 1)

# 정수 집합에서 정의된 자기 자신을 제외한 최소 상계
L = lambda x: ceil(x - 1)

def impl1():
    s = 'abcde5'
    i = U(len(s) / 2)
    j = L(len(s) / 2)
    while 0 <= j and i < len(s):
        print(j, i)
        i += 1
        j -= 1

def impl2():
    s = '123456789'
    i = 0
    j = len(s) - 1
    while i < j:
        print(i, j)
        i += 1
        j -= 1

def impl3():
    s = '01245'
    print(s[:floor(len(s) / 2)])
    print(s[:L(len(s) / 2):-1])

def impl4():
    s = '01234'
    print(s[len(s) // 2 - 1::-1])
    print(s[ceil(len(s) / 2):])
