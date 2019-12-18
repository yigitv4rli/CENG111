def fon(lst):
    for i in range(0,len(lst[0])):
        total = 0
        for j in range(0,len(lst[0])):
            total += lst[j][i]
            if j != i:
                lst[j][i] = '*'
        lst[i][i] = total
    return lst
liste = [[1,2,3],[1,2,3],[1,2,3]]

print(fon(liste))