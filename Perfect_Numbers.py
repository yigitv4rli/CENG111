def summation(N):
    total = 0
    for i in range(1,N):
        if N%i == 0:
            total += i
    return total

def perfect_numbers(N):
    div = [],[],[]
    for i in range(1,N):
        if summation(i) == i:
            div[0].append(i)
        elif summation(i) > i:
            div[1].append(i)
        elif summation(i) < i:
            div[2].append(i)
    return div
