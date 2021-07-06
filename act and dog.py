for i in range(int(input())):
    c, d, l=map(int, input().split())
    cog = (l - 4 * d) // 4
    cod = c - cog
    if l % 4 == 0 and l <= 4 * (c + d) and l >= 4 * d and cod <= 2 * d:
        print('yes')
    else:
        print('no')