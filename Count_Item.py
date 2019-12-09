def count_item(arg, lst):
    if lst == []:
        return 0
    if arg == lst[0]:
        return 1 + count_item(arg, lst[1:])
    else:
        return 0 + count_item(arg, lst[1:])
    	