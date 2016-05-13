# -*- coding: UTF-8 -*-

radixPrime = 127

ord_a = ord('a')

def new_vigenere_table(keywords):
    table = []
    for i in range(len(keywords)):
        row = []
        row.extend(keywords[i:])
        row.extend(keywords[:i])
        table.append(row)

    return table

VigenereTableau = new_vigenere_table(" abcdefghijklmnopqrstuvwxyz")

def new_window(pattern):
    window = 0
    power = pow(radixPrime, len(pattern))

    for char in pattern:
        window = window * radixPrime + ord(char)

    return window, power

def index_char(text, char):
    for pos, x in enumerate(text):
        if char == x:
            return pos

    return -1

def index_short_pattern(text, pattern):
    n = len(pattern)
    for pos in range(len(text) - n + 1):
        if text[pos:pos + n] == pattern:
            return pos

    return -1

def index_rp(text, pattern):
    n = len(pattern)
    if n == 0:
        return 0

    if len(text) < n:
        return -1

    if n == 1:
        return index_char(text, pattern)

    if len(text) == n:
        return text != pattern and -1 or 0

    if len(text) < 32:
        return index_short_pattern(text, pattern)

    hash, power = new_window(pattern)
    window = 0

    for pos in range(n):
        window = window * radixPrime + ord(text[pos])

    if hash == window:
        if text[:n] == pattern:
            return 0

    pos = n
    ntext = len(text)
    while pos < ntext:
        window = window * radixPrime + ord(text[pos])
        window -= power * ord(text[pos - n])
        pos += 1
        if window == hash:
            if text[pos - n:pos] == pattern:
                return pos - n

    return -1

def find_all_email(src):
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

# 첫 번째 문제
def P1():
    a = vigenere_encrypt('attack safe zone', 'abc')
    b = 'bvwbenaudggc qqf'
    print(a)
    print(b)
    print(a == b)

# 첫 번째 문제 추가 과제
def P1_2():
    print(vigenere_encrypt('attack safe zone', 'abcdefghijk'))
    print(vigenere_encrypt('attack boring zone', 'tpwhdeodhkd'))
    print(vigenere_encrypt('modular multiplicative inverse', 'solving congruence'))

# 두 번째 문제
def P2():
    r = open('source.html', 'r', -1, 'utf-8')
    data = r.read()
    r.close()
    for addr in find_all_email(data):
        print(addr)

def main():
    P1()
    P1_2()
    P2()

if __name__ == '__main__':
    main()
