ls = list(map(int, input().split('+')))
ls = sorted(ls)
for i in range(len(ls)-1):
    print(ls[i], end='+')
else:
    print(ls[len(ls)-1])