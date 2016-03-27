# -*- coding: utf-8 -*-

PRINT_NEWLINE = -1
PRINT_RESET = -2

# 각 라인의 마지막에 공백이 포함되는 것을 원한다면 1,
# 그렇지 않다면 0
END_WITH_SPACE = 1

def needed_rows(n):
    j = 1
    v = 2
    n += 1
    while v < n:
        v <<= 1
        j += 1
    return j

def printer_without_space(old_state, new_state):
    if new_state == PRINT_NEWLINE:
        print(old_state)
        return PRINT_RESET
    if old_state >= 0:
        print(old_state, end=' ')
    return new_state

def printer_with_space(old_state, new_state):
    if new_state >= 0:
        print(new_state, end=' ')
    if new_state == PRINT_NEWLINE:
        print()
    return PRINT_RESET

if END_WITH_SPACE:
    printer = printer_with_space
else:
    printer = printer_without_space

def print_rows(n):
    j = needed_rows(n)
    printer_state = PRINT_RESET

    i = 1
    v = 1

    for _ in range(j - 1):
        for _ in range(v):
            printer_state = printer(printer_state, i)
            i += 1
        printer_state = printer(printer_state, PRINT_NEWLINE)
        v <<= 1

    for i in range(i, n + 1):
        printer_state = printer(printer_state, i)
    printer_state = printer(printer_state, PRINT_NEWLINE)

# e > 0 인 자연수이다.
def evalTerm(a, x, e):
    if a == 0:
        return 0
    if x == 0:
        return 0
    if x == 1:
        return a
    v = a
    for i in range(e):
        v *= x
    return v

# 문제 1 번
def Problem1():
    a = int(input("a = "))
    x = int(input("x = "))
    e = int(input("e = "))

    print("계산 결과 :", evalTerm(a, x, e))

# 문제 2 번
def Problem2():
    n = int(input("N = "))
    print_rows(n)

