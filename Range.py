def myrange(start, end, step):
    if start >= end:
        return []
    else:
        return [start] + myrange(start+step,end,step)