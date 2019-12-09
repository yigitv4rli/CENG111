def is_substring(var1, var2):
    if len(var1) > len(var2):
        return False
    elif var1 == var2[:len(var1)]:
        return True
    else:
        return is_substring(var1, var2[1:])
        