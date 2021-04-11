n=int(input('Enter the number'))
for i in range(n+1):
    for j in range(1, i):
        print(j, end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()