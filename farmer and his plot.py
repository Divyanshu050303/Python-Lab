from math import gcd
for i in range(int(input())):
    n, m=list(map(int, input().split()))
    g=gcd(n, m)
    n, m=n//g, m//g
    l=int((n*m)/gcd(n, m))
    print(l)