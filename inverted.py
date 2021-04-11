n=int(input('Enter the number'))
for i in range(0, n):
    for j in range(n, i, -1):
        print(j, end='')
    for l in range(i+1):
        print('', end='')
    for j in range(i+1, n+1):
        print(j, end='')
    print('\n')