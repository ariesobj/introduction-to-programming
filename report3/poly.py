# -*- coding: UTF-8 -*-

def where_to_put(expr, power):
    # O(log(expr))

    if not expr:
        return 0

    i = 0
    j = len(expr) - 1

    while i <= j:
        med = (i + j) >> 1
        medpower = expr[med][0]
        if medpower > power:
            i = med + 1
        elif medpower < power:
            j = med - 1
        else:
            return

    return i

def inputPoly():
    # 총 N 번의 입력이 주어졌을 때,
    # O(NlogN)

    expr = []

    while True:
        power = int(input('지수 : '))
        coeff = int(input('계수 : ')) # R? Z+?

        if power < 0:
            print('다항식 리스트 :', expr)
            return

        index = where_to_put(expr, power)
        if index is None:
            print('같은 지수 값을 가지는 원소가 있습니다.')
            continue

        expr.insert(index, [power, coeff])

def sgn(n):
    '''Get the sign of a real number

    https://en.wikipedia.org/wiki/Sign_function'''

    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def printPoly(expr):
    ret = ''

    for power, coe in expr:
        if coe == 0:
            continue

        buf = ''
        if ~sgn(coe): # 1
            if ret:
                buf += ' + '
        else: # -1
            if ret:
                buf += ' - '
            else:
                buf += '-'

            coe *= -1

        if coe != 1:
            buf += str(coe)
        elif power == 0:
            buf += '1'

        if power > 1:
            buf += 'x^%d' % power
        elif power == 1:
            buf += 'x'

        ret += buf

    print('다항식 리스트 :', expr)
    print('다항식 =', ret)

    return ret

def addPoly(A, B):
    # O(max(A, B))

    C = []

    while A and B:
        powerA, coeA = A[0]
        powerB, coeB = B[0]

        if powerA > powerB:
            # 다항식의 덧셈은 immutable 한데 반해 리스트는 mutable 하므로
            # 새로운 리스트를 만들어 주어야 한다.
            C.append([powerA, coeA])
            A = A[1:]
        elif powerA < powerB:
            C.append([powerB, coeB])
            B = B[1:]
        else:
            coe = coeA + coeB
            if coe > 0:
                C.append([powerA, coe])

            A = A[1:]
            B = B[1:]

    if A:
        C.extend([x, y] for x, y in A)
    if B:
        C.extend([x, y] for x, y in B)

    return C

def multiplyPoly(A, B):
    # O(A(B + O(max(A, B))) = O(AB + max(A^2, AB)) = O(max(2AB, A^2 + AB)) = O(A(A+B))
    # O(nlogn) 까지 줄일 수 있나?

    A = A.copy()
    C = []

    while A:
        powerA, coeA = A.pop(0)
        D = [[powerA + powerB, coeA * coeB] for powerB, coeB in B]
        if C:
            C = addPoly(C, D)
        else:
            # avoid first copy
            C = D

    return C

def test1():
    A = [[5, 3], [3, 5], [1, 4], [0, 2]]
    B = [[5, 2], [2, 4], [1, 3]]
    C = addPoly(A, B)

    printPoly(A)
    printPoly(B)
    printPoly(C)

def test2():
    A = [[3, 2], [2, 3], [0, 1]]
    B = [[2, 3], [0, 2]]
    C = multiplyPoly(A, B)
    printPoly(A)
    printPoly(B)
    printPoly(C)
