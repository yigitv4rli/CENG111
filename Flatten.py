def flatten(lst):
    flatted = []
    flat = True
    while flat:
        flat = False
        first = lst[0]
        lst = lst[1:]
        if type(first) == list:
            lst += first
            flat = True 
        else:
            flatted.append(first)
    return flatted