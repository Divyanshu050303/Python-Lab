for i in range(int(input())):
    n = int(input())
    s = input()
    r = 0
    g = 0
    b = 0
    for j in s:
        if j == 'R':
            r = r + 1
        elif j == 'G':
            g = g + 1
        elif j == 'B':
            b = b + 1

    if r == g == b:
        print(2 * r)
    else:
        s = r + g + b
        m = max(r, g, b)
        print(s - m)
