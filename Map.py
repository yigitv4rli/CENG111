def every(func, lst):
    if lst == []:
        return []
    else:
        return [func(lst[0])] + every(func, lst[1:])