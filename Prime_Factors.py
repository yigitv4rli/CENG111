def isPrime(N):
    a = 2 
    while a <= N**0.5:
        if N % a == 0:
            return False
        else:
            a +=1
    return True

def listPrime(M):
    arr = []
    for i in range(2,M+1):
        if isPrime(i) == True:
            arr.append(i)
    return arr

def prime_factors(a):
    arr = listPrime(a)
    factors = []
    for i in arr:
        if a % i == 0:
            factors.append(i)
    return factors