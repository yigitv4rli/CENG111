def remove_item(arg, lst):
    if lst == []:
        return []
    elif arg == lst[0]:
        return remove_item(arg, lst[1:])
    else:
        return [lst[0]] + remove_item(arg, lst[1:])