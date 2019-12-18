def split(arg, seperator):
    splitted = []
    word = ""
    if len(arg) == 0:
        return ['']
    
    for char in arg:
        if char not in seperator:
            word += char
        else:
            splitted.append(word)
            word = ""
    splitted.append(word)
    return splitted
