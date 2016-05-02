from math import sqrt, trunc

# sqrtz: Z+ -> Z+ AND sqrtz(n) <= sqrt(n) 을 만족하는 함수를 구현한다.
def sqrtz(n):
    return trunc(sqrt(n))

# 이전에 이미 소인수가 발견되었음을 활용한다.
def assemble_factor(n):
    factors = {}
    while not n & 1:
        n >>= 1
        factors[2] = factors.get(2, 0) + 1

    factor = 3

    # 1. p is prime iff there exists n such that p mod n = 0 and 1 < n <= sqrt(p)
    # 2. n is composite number iff n can be represented as ab (a, b less than sqrt(n))
    #
    # 간단한 소수 판정법에 흔히 사용되는 페르마의 작은 정리 1번과
    # 너무나도 자명안 합성수 2번을 활용하여 단순하게 +2 식 증가시키는
    # 방법보다 더 빠르게 소인수 분해해준다.
    #
    # ab = p, <x> = p, p/n1, p/n1n2, ...
    # -> <y> = <x> / <n> --- 식 1
    #
    # yn = sqrt(n) 이 아니다.
    # 왜냐하면 반복 순서와 깊은 관련이 있는데, sqrt(n) 으로 해놓으면
    # 동일한 sqrt(nj) 로 두 번을 나누기 때문이다.
    # 따라서 n 으로 해놓아서 한 번만 나누게 해준다.
    yn = n

    while n > 1 and factor <= yn:
        d, r = divmod(n, factor)
        if not r:
            if factors.get(factor) is None:
                # 식 1
                yn /= sqrt(factor)
            factors[factor] = factors.get(factor, 0) + 1
            n = d
        else:
            factor += 2

    return factors

def correctness(n):
    factors = assemble_factor(n)
    m = 1
    for p, times in factors.items():
        m *= p ** times

    print(factors)
    print(n, n == m and 'correct' or 'incorrect')

def is_prime(n):
    factors = assemble_factor(n)
    return _factors_of_prime(factors)

def _factors_of_prime(factors):
    if len(factors) > 1:
        return False
    for times in p.values():
        if times > 1:
            return False
    return True

def x111():
    n = 1
    while True:
        yield n
        n *= 10
        n += 1

def main():
    gen = x111()
    next(gen) # 1
    next(gen) # 11

    for i in range(10):
        n = i + 2
        factors = assemble_factor(next(gen))
        print('p_' + str(n), _factors_of_prime(factors), factors)

if __name__ == '__main__':
    main()
