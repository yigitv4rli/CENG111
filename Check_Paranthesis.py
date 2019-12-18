def checkParanthesis(var):
    chrOpen = ["{","(","["]
    chrClose = ["}",")","]"]
    stack = []
    for char in var:
        if char in chrOpen:
            stack.append(char)
        elif char in chrClose:
            if len(stack) == 0:
                return False
            elif chrOpen.index(char) != chrOpen.index(stack.pop()):
                return False
    if len(stack) > 0:
        return False
    return True