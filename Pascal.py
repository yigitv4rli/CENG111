def pascal(N):
    arg = [[1],[1,1]]
    if N == 1:
        return [[1]]
    elif N == 2:
        return [[1],[1,1]]
    else:
    	count = 2
        while count < N:
            tri = []
            for i in range(0,len(arg[-1])-1):
                tri.append(arg[-1][i] + arg[-1][i+1])
            tri = [1]+tri+[1]
            arg.append(tri)
            count+=1
        return arg
