# -*- coding: utf-8 -*-
# 컴퓨터 공학부 201601560 권혁모

PRINT_NEWLINE = -1
PRINT_RESET = -2

# 개인적으로 각 라인 마지막에 공백이 포함되지 않는 것을 선호하므로
# 공백 유무에 따른 두 가지 경우를 모두 고려하여 프로그램이 작성되어 있다.
# 마지막에 공백이 없게 하고 싶으면 F, 그렇지 않으려면 T
END_WITH_SPACE = True

EASY_PRINT = True

# 첫 번째 문제
def evalTerm(a, x, e):
    if a == 0:
        return 0
    if x == 0:
        if e == 0:
            return a
        else:
            return 0
    if x == 1:
        return a
    v = a
    for i in range(e):
        v *= x
    return v

# 두 번째 문제
def print_rows(n):
    j = compute_needed_rows(n)
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

def compute_needed_rows(n):
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

def printer(x, y):
    if END_WITH_SPACE:
        return printer_with_space(x, y)
    else:
        return printer_without_space(x, y)

def testify_correctness(fn, cases):
    for (*args, expected) in cases:
        equated = fn(*args)
        assert equated == expected, "{}{} expected {}, but got {}".format(
            fn.__name__, tuple(args), expected, equated)
        if EASY_PRINT:
            print("{}{} = {}".format(fn.__name__, tuple(args), equated))

def main():
    testify_correctness(evalTerm, [
        (1, 0, 0, 1),
        (9, 0, 0, 9),
        (0, 0, 0, 0),
        (2, 2, 3, 16),
        (4, 0, 5, 0),
        (3, 0, 0, 3),
        (5, 3, 0, 5),
        (1, 1, 1, 1),
        (4, 3, 2, 36),
    ])

    print()
    print('N', '=', 10)
    print_rows(10)

    print()
    print('N', '=', 20)
    print_rows(20)

if __name__ == '__main__':
    main()
