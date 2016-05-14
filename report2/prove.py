# -*- coding: UTF-8 -*-

from contextlib import contextmanager
import random

DO_VERIFICATION = True

some_alphabet_ords = [ord(' ')]
some_alphabet_ords.extend(i for i in range(ord('a'), ord('z') + 1))
some_alphabet_ords.extend(i for i in range(ord('A'), ord('Z') + 1))

def prepend(iterable, obj):
    yield obj
    yield from iterable

def _PMFR_iterator(z, space, yield_elem):
    w = 0
    for obj, p in space:
        real = p / (z - w)
        w += p
        if random.random() < real:
            if yield_elem:
                yield (obj, p)
            else:
                yield obj
            return w

    # BUG: FPMFRU(some_alphabet_ords, n)
    # 문제가 발생한다... 무엇이 잘못된지 모르겠다... 나중에 시간 날 때 하자...

    # 확률질량함수가 입력으로 주어지지 않았다면 이 부분이 실행될 수 있다.
    # 그렇지 않다면 이 부분은 절대 실행되지 않음이 수학적으로 보장된다.
    raise ValueError('probability mass function is not provided')

# (x, p)
def PMFR(space, r, yield_elem=False):
    space = iter(space)
    keep = [elem for _, elem in zip(range(r), space)]
    if len(keep) < r:
        return []

    z = 1 - sum(p for obj, p in keep)

    for i in range(r):
        obj, pro = keep.pop()
        z += pro
        z -= yield from _PMFR_iterator(z, prepend(space, (obj, pro)), yield_elem)

# with finite uniform distribution
def FPMFRU(finite, r):
    p = 1 / len(finite)

    def space():
        for obj in finite:
            yield obj, p

    return PMFR(space(), r)

def alphastr(n):
    line = bytearray(random.choice(some_alphabet_ords) for i in range(n))
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