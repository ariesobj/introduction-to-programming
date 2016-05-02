def poprime(n):
    if n <= 1:
        return []
    if n == 2:
        return [2]

    p = list(range(3, n+1, 2))
    j = 1
    while j < len(p):
        q = r = p[0]
        i = 1
        while i < len(p):
            # 각 원소에 숫차적으로 접근하기 때문에 더이상 mod를 사용할 필요가 없음
            if p[i] == q:
                q += r
                p.pop(i)
            else:
                i += 1
        j += 1

    return p