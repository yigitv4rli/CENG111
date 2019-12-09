def triangle(N):
    tri = []
    for i in range(1,N+1):
        space = N - i
    	star = 2*i - 1
        tri.append(space * " " + star * "*")
    return tri