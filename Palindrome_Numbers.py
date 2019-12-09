def palindromes(N):
    arr = []
    for i in range(0,N+1):
        if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]:
            arr.append(i)
    return arr