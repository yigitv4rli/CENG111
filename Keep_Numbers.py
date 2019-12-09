def keep_numbers(lst):
    if lst == []:
        return []
    elif type(lst[0]) == int or type(lst[0]) == float:
        return [lst[0]] + keep_numbers(lst[1:])
    else:
        return keep_numbers(lst[1:])