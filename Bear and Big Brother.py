def big(a, b):
    i = 0
    while a <= b:
        a, b, i = a*3, b*2, i+1
    print(i)


x, y = map(int, input().split())
big(x, y)