def fibseries(N,previous=0,current=1):
    if N == 1:
        return [previous]
    else:
        return [previous] + fibseries(N-1,current,previous+current)