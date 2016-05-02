# eratosthenes sieve
def sieve(n):
    if n <= 1:
        return []
    
    daisy = first_chain
    primes = [2]
    for i in range(3, n+1, 2):
        p = daisy(i)
        if p:
            daisy = chain(p, daisy)
            primes.append(p)
            
    return primes 

# No lambda
def first_chain(devidend):
    if devidend & 1:
        return devidend

# No lambda
def chain(least, climb):
    def inner(devidend):
        if devidend % least:
            return climb(devidend)
    
    return inner
