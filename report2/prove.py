# -*- coding: UTF-8 -*-

from contextlib import contextmanager
import random

DO_VERIFICATION = True

some_alphabets = [ord(' ')]
some_alphabets.extend(i for i in range(ord('a'), ord('z') + 1))
some_alphabets.extend(i for i in range(ord('A'), ord('Z') + 1))

##def PMF(poss):
##    z = 0
##    for (p, v) in poss:
##        if random.random() < p / (1 - z):
##            return v
##        z += p
##
##    # unreachable
##    #
##    # 그러나 함수가 확률질량함수를 이루지 못했을 때 이 코드가 실행될 수도 있음.

##def equalize_poss(lst):
##    n = 1 / len(lst)
##    for elem in lst:
##        yield (n, elem)

def alphastr(n):
    line = bytearray(random.choice(some_alphabets) for i in range(n))
    line = line.decode()
    return line

class Failure(Exception):
    pass

class Incorrect(Failure):
    def __init__(self, name, args, expected, ret):
        super().__init__()
        self.name = name
        self.args = args
        self.expected = expected
        self.ret = ret

    def __str__(self):
        return "{}{} expected {} but returned {}".format(
            self.name, self.args, self.expected, self.ret)

# TDT (Table Driven Test)
def do_TDT(fn, cases):
    for args, expected in cases:
        ret = fn(*args)
        if ret != expected:
            raise Incorrect(fn.__name__, args, expected, ret)

def do_comparison(fn, proven, inargs):
    for args in inargs:
        expected = proven(*args)
        ret = fn(*args)
        if expected != ret:
            raise Incorrect(fn.__name__, args, expected, ret)

def str_supplier(repeat, maxlen):
    for i in range(repeat):
        n = random.randint(0, maxlen)
        m = random.randint(0, n)
        yield alphastr(n), alphastr(m)

def proven_index_fn(raw, sep):
    return raw.find(sep)

def verify_index_fn():
    try:
        from report import index_char, index_short_pattern, index_rp
    except ImportError:
        raise Failure("cannot import module report")

    index_char_table = [
        (('abcdefg', 'f'), 5),
        (('abcdefg', 'b'), 1),
        (('abcdefg', 'a'), 0),
        (('abcdefg', 'h'), -1),
    ]

    index_short_pattern_table = [
        (('abcdefg', 'def'), 3),
        (('abcdefg', 'abc'), 0),
        (('abcdefg', 'abg'), -1),
    ]

    index_rp_table = [
        (('abcde', 'cde'), 2),
        (('19232', '233'), -1),
        (('2982',  '82'), 2),
        (('01231654658976564654654654132134657468787974',  '7974'), 40),
        (('01231654658976564654654654132134657468787974',  '10100000'), -1),

    ]
    index_rp_table.extend(index_char_table)
    index_rp_table.extend(index_short_pattern_table)

    do_TDT(index_char, index_char_table)
    do_TDT(index_short_pattern, index_short_pattern_table)
    do_TDT(index_rp, index_rp_table)

    do_comparison(index_rp, proven_index_fn, str_supplier(500, 1000))

@contextmanager
def verifier():
    try:
        yield
    except Failure as fail:
        print(fail)

def main():
    if DO_VERIFICATION:
        with verifier():
            verify_index_fn()

if __name__ == '__main__':
    main()