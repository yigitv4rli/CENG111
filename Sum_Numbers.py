def sum_numbers(arg):
    if arg == [] : return 0
    elif type(arg[0]) == int or type(arg[0]) == float:
        a = arg[0] 
        return arg[0] + sum_numbers(arg[1:])
    else:
        return sum_numbers(arg[1:])