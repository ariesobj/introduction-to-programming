# -*- coding: UTF-8 -*-

nan = float('nan')

def anahash(s, bits):
    h = 0
    b = ~-(1 << bits)
    for c in s:
        shift = ord(c) * bits
        i = b << shift
        v = (h & i) >> shift
        if v >= b:
            # raise
            # 사용 가능한 비트 수 한계로 계산 불가능
            return nan

        v += 1
        h |= i
        h ^= (v ^ b) << shift

    return h

# 각 문자당 bits 개의 비트를 사용하여 두 문자열이 어구 전철(anagram)인지 판단한다.
#
#   n = 1 << bits
#
# 구현 방식에 의해 한 문자가 n 개 이상 나오는 문자에 대하여 어구 전철인지
# 판단할 수 없습니다.
def is_anagram(a, b, bits=8):
    return anahash(a, bits) == anahash(b, bits)

