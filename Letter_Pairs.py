def letter_pairs(arg):
    if len(arg) <= 1:
        return []
    else:
        return [arg[:2]] + letter_pairs(arg[1:])