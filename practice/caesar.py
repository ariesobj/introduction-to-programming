# -*- coding: utf-8 -*-

ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')
ord_Z = ord('Z')
nalpha = ord_z - ord_a + 1

def isalpha(char):
    n = ord(char)
    if 0x0041 <= n <= 0x005a:
        return True
    if 0x0061 <= n <= 0x007a:
        return True
    return False

def _rotate(chars, rot):
    # https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
    #
    # The modulo operator always yields a result with the same sign as its
    # second operand (or zero); the absolute value of the result is strictly
    # smaller than the absolute value of the second operand
    #
    # 파이선 모듈로 연산은 위와 같이 잘 정의되어 있으므로 음수에 대해서 걱정할 필요가 없다.
    rot = rot % nalpha
    if rot == 0:
        return chars

    if rot < 0:
        pass

    # bytearray with len = len(chars)
    buffer = ""

    for char in chars:
        # BUG: str.isalpha 는 alphabetic 검사를 unicode 에 대해 적절하게 수행하지 못한다.
        # 예로 '가'.isalpha() 는 T 를 반환한다.
        if not isalpha(char):
            # TODO: frequent memory allocation
            buffer += char
            continue

        if char.islower():
            n = (ord(char) - ord_a + rot) % nalpha
            n += ord_a
        else:
            n = (ord(char) - ord_A + rot) % nalpha
            n += ord_A

        # TODO: frequent memory allocation
        buffer += chr(n)

    return buffer

def encipher(chars, rot):
    return _rotate(chars, rot)

def decipher(chars, rot):
    return _rotate(chars, -rot)