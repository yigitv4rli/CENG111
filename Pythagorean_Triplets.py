def isTriplets(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
def triplets(N):
    arr = []
    for i in range(1,N):
        for j in range(1,N):
            for m in range(1,N):
                if isTriplets(i,j,m) == True and ((j,i,m)) not in arr:
                    arr.append(tuple((i,j,m)))
    return arr