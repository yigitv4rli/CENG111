def keep(func, lst):
    if lst == []:
        return []
    elif func(lst[0]) == True:
        return [lst[0]] + keep(func,lst[1:])
    else:
        return keep(func,lst[1:])