# -*- coding: UTF-8 -*-

radPrime = 127
modPrime = 1000000007

max_short_string_len = 1 << 5

VigenereTableau = []
VigenereTableauKeywords = " abcdefghijklmnopqrstuvwxyz"

for i in range(len(VigenereTableauKeywords)):
    row = []
    row.extend(VigenereTableauKeywords[i:])
    row.extend(VigenereTableauKeywords[:i])
    VigenereTableau.append(row)

ord_a = ord('a')

def rolling_hash(chars):
    h = 0
    for char in chars:
        h = h*radPrime + ord(char)
    return h

def index_char(string, char):
    for i, x in enumerate(string):
        if x == char:
            return i
    return -1

def index_short_string(string, sep):
    for i in range(len(string) - len(sep) + 1):
        if string[i:i+len(sep)] == sep:
            return i

    return -1

def index_rp(string, sep):
    n = len(sep)
    if n == 0:
        return 0

    if len(string) < n:
        return -1

    if n == 1:
        return index_char(string, sep)

    if len(string) == n:
        if string == sep:
            return 0
        return -1

    if len(string) < max_short_string_len:
        return index_short_string(string, sep)

    h, p = rolling_hash(sep)
    p = n - 1
    u = 0
    for i in range(n):
        u = (u << 3) + ord(string[i])

    if u == h and string[:n] == sep:
        return 0

    i = n
    while i < len(string):
        u -= ord(string[i - n]) << p
        u = u * radixPrime + ord(string[i])
        i += 1
        if u == h and string[i-n:i] == sep:
            return i - n

    return -1

def find_all_addresses(src):
    MAIL_BEGIN = 'mailto:'
    MAIL_END = '"'

    addrs = []

    while src:
        i = index_rp(src, MAIL_BEGIN)
        if not ~i:
            break

        src = src[i + len(MAIL_BEGIN):]
        j = index_rp(src, MAIL_END)
        if not ~j:
            break

        addr = src[:j]
        src = src[j:]
        addrs.append(addr)

    return addrs

def char_number(char):
    if char == ' ':
        return 0

    char = char.lower()
    return ord(char) - ord_a + 1

def vigenere_encrypt(raw, keywords):
    pos = 0
    buf = ''
    for char in raw:
        kwdn = char_number(keywords[pos % len(keywords)])
        pos += 1
        buf += VigenereTableau[kwdn][char_number(char)]

    return buf

# 첫 번째 문제 해답
def P1():
    a = vigenere_encrypt('attack safe zone', 'abc')
    b = 'bvwbenaudggc qqf'
    print(a)
    print(b)
    print(a == b)

# 추가 과제
def P1_2():
    print(vigenere_encrypt('attack safe zone', 'abcdefghijk'))
    print(vigenere_encrypt('attack boring zone', 'tpwhdeodhkd'))
    print(vigenere_encrypt('modular multiplicative inverse', 'solving congruence'))

# 두 번째 문제 해답
def P2():
    # Py_DECREF 가 refcount 를 0 으로 만들꺼니까 FD Leak 을 못잡아내진 않는다.
    # ResourceWarning 은 무시하자
    src = open('source', encoding='utf-8').read()
    for address in find_all_addresses(src):
        print(address)

