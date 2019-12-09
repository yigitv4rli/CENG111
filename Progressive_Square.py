def progressive_square(arg):
    if len(arg) <= 1:
        return True
    ps = arg[0]**2 == arg[1]
    return ps and progressive_square(arg[1:])