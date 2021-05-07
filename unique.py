def lst(n):
    s=[]
    for i in n:
        if i not in s:
            s.append(i)
    return s


print(lst([1, 2, 3, 3, 3, 3, 4, 5]))